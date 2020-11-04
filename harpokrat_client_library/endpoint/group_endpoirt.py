#!/usr/bin/env python3
from harpokrat_client_library.api import Api
from harpokrat_client_library.endpoint.resource_endpoint import ResourceEndpoint


class GroupEndpoint(ResourceEndpoint):
    def __init__(self, api: Api, uri: str):
        super().__init__(api, '{}/groups'.format(uri), 'groups')
