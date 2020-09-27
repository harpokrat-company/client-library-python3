#!/usr/bin/env python3
from hclw.HCLW import HCLW

from harpokrat_client_library.models.response import HarpokratResponse
from harpokrat_client_library.models.relationship import Relationship
from harpokrat_client_library.models.resource_identifier import ResourceIdentifier
from harpokrat_client_library.services.api_service import ApiService
from harpokrat_client_library.services.auth_service import AuthService
from harpokrat_client_library.services.password_service import PasswordService


class UserPasswordService(PasswordService):
    def __init__(self, api_service: ApiService, auth_service: AuthService, uri: str, wrapper: HCLW):
        super().__init__(api_service, auth_service, uri, wrapper)

    def create(self, password, relationships=None) -> HarpokratResponse:
        if relationships is None:
            relationships = {}
        relationships['owner'] = Relationship(ResourceIdentifier('users', self.auth_service.user_id))
        return super().create(password, relationships)
