#!/usr/bin/env python3
from HarpokratClientLibrary.models.HarpokratResponse import HarpokratResponse
from HarpokratClientLibrary.services.AuthService import AuthService
from HarpokratClientLibrary.services.UserService import UserService


class MeService:
    def __init__(self, auth_service: AuthService, user_service: UserService):
        self.auth_service = auth_service
        self.user_service = user_service

    def me(self) -> HarpokratResponse:
        if self.auth_service.user_id is None:
            raise
        return self.user_service.read(self.auth_service.user_id)
