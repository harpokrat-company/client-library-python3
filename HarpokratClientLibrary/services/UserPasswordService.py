#!/usr/bin/env python3
from HarpokratClientLibrary.models.HarpokratResponse import HarpokratResponse
from HarpokratClientLibrary.models.Relationship import Relationship
from HarpokratClientLibrary.models.ResourceIdentifier import ResourceIdentifier
from HarpokratClientLibrary.services.ApiService import ApiService
from HarpokratClientLibrary.services.AuthService import AuthService
from HarpokratClientLibrary.services.PasswordService import PasswordService


class UserPasswordService(PasswordService):
    def __init__(self, api_service: ApiService, auth_service: AuthService, uri: str):
        super().__init__(api_service, uri)
        self.auth_service = auth_service

    def create(self, password, relationships=None) -> HarpokratResponse:
        if relationships is None:
            relationships = {}
        relationships['owner'] = Relationship(ResourceIdentifier('users', self.auth_service.user_id))
        return super().create(password, relationships)
