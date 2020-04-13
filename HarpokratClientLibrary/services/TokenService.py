#!/usr/bin/env python3
import base64

from HarpokratClientLibrary.models.HarpokratResponse import HarpokratResponse
from HarpokratClientLibrary.models.domain.User import User
from HarpokratClientLibrary.services.ApiService import ApiService
from HarpokratClientLibrary.services.AuthService import AuthService
from HarpokratClientLibrary.services.ResourceService import ResourceService
from hclw.HCLW import HCLW


class TokenService:
    def __init__(self, wrapper: HCLW, api_service: ApiService, auth_service: AuthService, uri: str):
        self.uri = '{}/json-web-tokens'.format(uri)
        self.api = api_service
        self.auth = auth_service
        self.wrapper = wrapper

    def login(self, email: str, password: str) -> HarpokratResponse:
        header = {
            'Authorization': self.wrapper.get_basic_auth(email, password)
        }
        response = self.api.post(self.uri, headers=header)
        harpokrat_response = HarpokratResponse.construct_from(response)
        self.auth.token = harpokrat_response.data.attributes.token
        self.auth.user_id = harpokrat_response.data.relationships['user'].data.id
        self.auth.key = password  # TODO : remove this
        return harpokrat_response
