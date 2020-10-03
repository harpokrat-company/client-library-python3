#!/usr/bin/env python3
from hclw.HCLW import HCLW

from harpokrat_client_library.services.api_service import ApiService
from harpokrat_client_library.services.auth_service import AuthService
from harpokrat_client_library.services.me_service import MeService
from harpokrat_client_library.services.password_service import PasswordService
from harpokrat_client_library.services.secret_service import SecretService
from harpokrat_client_library.services.token_service import TokenService
from harpokrat_client_library.services.user_password_service import UserPasswordService
from harpokrat_client_library.services.user_service import UserService


class Harpokrat:
    def __init__(self, uri: str):
        self.uri = uri
        self.wrapper = HCLW()
        self._init_services()

    def _init_services(self):
        # TODO : refactor this
        self.wrapper = HCLW()

        self.auth_service = AuthService()
        self.api_service = ApiService(self.auth_service)

        self.token_service = TokenService(self.wrapper, self.api_service, self.auth_service, self.uri)
        self.user_service = UserService(self.wrapper, self.api_service, self.uri)
        self.me_service = MeService(self.auth_service, self.user_service)

        self.secret_service = SecretService(self.api_service, self.auth_service, self.uri, self.wrapper)
        self.password_service = PasswordService(self.api_service, self.auth_service, self.uri, self.wrapper)
        self.user_password_service = UserPasswordService(self.api_service, self.auth_service, self.uri, self.wrapper)
