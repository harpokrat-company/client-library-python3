#!/usr/bin/env python3
from harpokrat_client_library.models.relationship import Relationship
from harpokrat_client_library.models.resource_identifier import ResourceIdentifier
from harpokrat_client_library.services.password_service import PasswordService


class UserPasswordService(PasswordService):
    def create(self, attributes, relationships=None):
        if relationships is None:
            relationships = {}
        relationships['owner'] = Relationship(ResourceIdentifier('users', self.auth_service.user_id))
        return super().create(attributes, relationships)
