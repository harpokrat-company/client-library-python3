#!/usr/bin/env python3
from hclw.HCLW import HCLW

from HarpokratClientLibrary.models.HarpokratResponse import HarpokratResponse
from HarpokratClientLibrary.models.domain.User import User
from HarpokratClientLibrary.services import ApiService
from HarpokratClientLibrary.services.ResourceService import ResourceService


class UserService(ResourceService):
    def __init__(self, wrapper: HCLW, api_service: ApiService, uri: str):
        super().__init__(api_service, '{}/{}'.format(uri, 'users'), 'users')
        self.wrapper = wrapper

    def create(self, attributes: User, relationships=None) -> HarpokratResponse:
        return super().create(
            User(attributes.email, self.wrapper.get_derived_key(attributes.password), attributes.firstName, attributes.lastName),
            relationships
        )

    def update(self, resource_id, attributes, relationships=None) -> HarpokratResponse:
        raise Exception("not implemented")
