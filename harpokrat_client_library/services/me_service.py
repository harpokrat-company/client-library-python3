#!/usr/bin/env python3
from harpokrat_client_library.models.response import HarpokratResponse
from harpokrat_client_library.services.auth_service import AuthService
from harpokrat_client_library.services.user_service import UserService


class MeService:
    def __init__(self, auth_service: AuthService, user_service: UserService):
        self.auth_service = auth_service
        self.user_service = user_service

    def me(self) -> HarpokratResponse:
        if self.auth_service.user_id is None:
            raise
        return self.user_service.read(self.auth_service.user_id)
