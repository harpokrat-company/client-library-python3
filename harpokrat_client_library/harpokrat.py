#!/usr/bin/env python3
from hclw.HCLW import HCLW

from harpokrat_client_library.api import Api
from harpokrat_client_library.authentication import Authentication
from harpokrat_client_library.services.me_service import MeService
from harpokrat_client_library.services.password_service import PasswordService
from harpokrat_client_library.endpoint.secret_endpoint import SecretEndpoint
from harpokrat_client_library.endpoint.token_endpoint import TokenEndpoint
from harpokrat_client_library.endpoint.user_endpoint import UserEndpoint


class Harpokrat:
    def __init__(self, uri: str):
        self.uri = uri
        self.wrapper = HCLW()
        self._init_services()

    def _init_services(self):
        # TODO : refactor this
        self.wrapper = HCLW()

        self.auth = Authentication()
        self.api = Api(self.auth)

        self.token_endpoint = TokenEndpoint(self.wrapper, self.api, self.auth, self.uri)
        self.user_endpoint = UserEndpoint(self.api, self.uri)
        self.secret_endpoint = SecretEndpoint(self.api, self.uri)

        self.me_service = MeService(self.auth, self.user_endpoint)
        self.password_service = PasswordService(self.user_endpoint, self.secret_endpoint, self.wrapper, self.auth)
