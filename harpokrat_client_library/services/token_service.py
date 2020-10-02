#!/usr/bin/env python3
from hclw.HCLW import HCLW

from harpokrat_client_library.services.api_service import ApiService
from harpokrat_client_library.services.auth_service import AuthService


class TokenService:
    def __init__(self, wrapper: HCLW, api_service: ApiService, auth_service: AuthService, uri: str):
        self.uri = '{}/json-web-tokens'.format(uri)
        self.api = api_service
        self.auth = auth_service
        self.wrapper = wrapper

    def login(self, email: str, password: str):
        header = {
            'Authorization': self.wrapper.get_basic_auth(email, password)
        }
        response = self.api.post(self.uri, headers=header)
        self.auth.token = response['data']['attributes']['token']
        self.auth.user_id = response['data']['relationships']['user']['data']['id']
        self.auth.key = self.wrapper.get_derived_key(password)
        return response
