#!/usr/bin/env python3
from HarpokratClientLibrary.services.ApiService import ApiService
from HarpokratClientLibrary.services.AuthService import AuthService
from HarpokratClientLibrary.services.TokenService import TokenService
from HarpokratClientLibrary.services.UserService import UserService


class HarpokratAPI:
    def __init__(self, uri: str):
        self.uri = uri
        self._init_services()

    def _init_services(self):
        self.auth_service = AuthService()
        self.api_service = ApiService(AuthService)
        self.token_service = TokenService(self.api_service, self.uri)
        self.user_service = UserService(self.api_service, self.uri)
