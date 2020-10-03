#!/usr/bin/env python3
from hclw.HCLW import HCLW

from harpokrat_client_library.services.api_service import ApiService
from harpokrat_client_library.services.auth_service import AuthService
from harpokrat_client_library.services.resource_service import ResourceService


class SecretService(ResourceService):
    def __init__(self, api_service: ApiService, auth_service: AuthService, uri: str, wrapper: HCLW):
        super().__init__(api_service, '{}/secrets'.format(uri), 'secrets')
        self.wrapper = wrapper
        self.auth_service = auth_service

    # TODO : temporary fix find a better way
    def filter_resource(self, resources):
        return list(
            filter(lambda x: x['relationships']['owner']['data']['id'] == self.auth_service.user_id, resources)
        )

    def read_all(self):
        response = super().read_all()
        response['data'] = self.filter_resource(response['data'])
        return response
