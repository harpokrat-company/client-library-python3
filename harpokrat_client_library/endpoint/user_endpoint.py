#!/usr/bin/env python3
from harpokrat_client_library.api import Api
from harpokrat_client_library.endpoint.resource_endpoint import ResourceEndpoint


class UserEndpoint(ResourceEndpoint):
    def __init__(self, api: Api, uri: str):
        super().__init__(api, '{}/{}'.format(uri, 'users'), 'users')

    def create(self, attributes, relationships=None):
        raise Exception("not implemented")

    def update(self, resource_id, attributes, relationships=None):
        raise Exception("not implemented")
