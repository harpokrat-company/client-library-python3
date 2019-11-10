#!/usr/bin/env python3
import base64

from HarpokratClientLibrary.models.HarpokratResponse import HarpokratResponse
from HarpokratClientLibrary.services.ApiService import ApiService
from HarpokratClientLibrary.services.AuthService import AuthService
from HarpokratClientLibrary.services.ResourceService import ResourceService


class TokenService(ResourceService):
    def __init__(self, api_service: ApiService, auth_service: AuthService, uri: str):
        super().__init__(api_service, '{}/json-web-tokens'.format(uri), 'tokens')
        self.auth_service = auth_service

    def login(self, email: str, password: str) -> HarpokratResponse:
        encoded = base64.b64encode('{}:{}'.format(email, password).encode('utf-8'))
        header = {
            'Authorization': 'Basic {}'.format(encoded.decode('utf-8'))
        }
        response = self.api.post(self.uri, headers=header)
        harpokrat_response = HarpokratResponse.construct_from(response)
        self.auth_service.token = harpokrat_response.data.attributes.token
        self.auth_service.user_id = harpokrat_response.data.relationships['user'].data.id
        return harpokrat_response
