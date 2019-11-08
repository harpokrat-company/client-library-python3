#!/usr/bin/env python3
from HarpokratClientLibrary.services import ApiService
from HarpokratClientLibrary.services.ResourceService import ResourceService


class UserService(ResourceService):
    def __init__(self, api_service: ApiService, uri: str):
        super().__init__(api_service, '{}/{}'.format(uri, 'users'), 'users')
