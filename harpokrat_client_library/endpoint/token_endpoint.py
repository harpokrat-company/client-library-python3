#!/usr/bin/env python3
from hclw.HCLW import HCLW

from harpokrat_client_library.api import Api
from harpokrat_client_library.authentication import Authentication


class TokenEndpoint:
    def __init__(self, wrapper: HCLW, api: Api, auth: Authentication, uri: str):
        self.uri = '{}/json-web-tokens'.format(uri)
        self.api = api
        self.auth = auth
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
