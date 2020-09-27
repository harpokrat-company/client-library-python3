#!/usr/bin/env python3
from hclw.HCLW import HCLW

from harpokrat_client_library.models.response import HarpokratResponse
from harpokrat_client_library.models.domain.user import User
from harpokrat_client_library.services import api_service
from harpokrat_client_library.services.resource_service import ResourceService


class UserService(ResourceService):
    def __init__(self, wrapper: HCLW, api_service: api_service, uri: str):
        super().__init__(api_service, '{}/{}'.format(uri, 'users'), 'users')
        self.wrapper = wrapper

    def create(self, attributes: User, relationships=None) -> HarpokratResponse:
        return super().create(
            User(attributes.email, self.wrapper.get_derived_key(attributes.password), attributes.firstName, attributes.lastName),
            relationships
        )

    def update(self, resource_id, attributes, relationships=None) -> HarpokratResponse:
        raise Exception("not implemented")
