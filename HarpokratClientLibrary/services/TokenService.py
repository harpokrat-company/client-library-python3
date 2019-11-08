#!/usr/bin/env python3
import base64

from HarpokratClientLibrary.models.HarpokratResponse import HarpokratResponse
from HarpokratClientLibrary.services import ApiService
from HarpokratClientLibrary.services.ResourceService import ResourceService


class TokenService(ResourceService):
    def __init__(self, api_service: ApiService, uri: str):
        super().__init__(api_service, '{}/json-web-tokens'.format(uri), 'tokens')

    def login(self, email: str, password: str):
        encoded = base64.b64encode('{}:{}'.format(email, password).encode('utf-8'))
        header = {
            'Authorization': 'Basic {}'.format(encoded.decode('utf-8'))
        }
        response = self.api.post(self.uri, headers=header)
        return HarpokratResponse.construct_from(response)
