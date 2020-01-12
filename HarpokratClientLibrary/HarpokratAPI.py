#!/usr/bin/env python3
from HarpokratClientLibrary.services.ApiService import ApiService
from HarpokratClientLibrary.services.AuthService import AuthService
from HarpokratClientLibrary.services.MeService import MeService
from HarpokratClientLibrary.services.PasswordService import PasswordService
from HarpokratClientLibrary.services.SecretService import SecretService
from HarpokratClientLibrary.services.TokenService import TokenService
from HarpokratClientLibrary.services.UserPasswordService import UserPasswordService
from HarpokratClientLibrary.services.UserService import UserService
from hclw.HCLW import HCLW


class HarpokratAPI:
    def __init__(self, uri: str):
        self.uri = uri
        self.wrapper = HCLW()
        self._init_services()

    def _init_services(self):
        # TODO : refactor this
        self.auth_service = AuthService()
        self.api_service = ApiService(self.auth_service)

        self.token_service = TokenService(self.wrapper, self.api_service, self.auth_service, self.uri)
        self.user_service = UserService(self.api_service, self.uri)
        self.me_service = MeService(self.auth_service, self.user_service)

        self.secret_service = SecretService(self.api_service, self.uri)
        self.password_service = PasswordService(self.api_service, self.uri)
        self.user_password_service = UserPasswordService(self.api_service, self.auth_service, self.uri)
