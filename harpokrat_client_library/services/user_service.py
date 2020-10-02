#!/usr/bin/env python3
from hclw.HCLW import HCLW

from harpokrat_client_library.services.api_service import ApiService
from harpokrat_client_library.services.resource_service import ResourceService


class UserService(ResourceService):
    def __init__(self, wrapper: HCLW, api_service: ApiService, uri: str):
        super().__init__(api_service, '{}/{}'.format(uri, 'users'), 'users')
        self.wrapper = wrapper

    def create(self, attributes, relationships=None):
        raise Exception("not implemented")

    def update(self, resource_id, attributes, relationships=None):
        raise Exception("not implemented")
