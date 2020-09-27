#!/usr/bin/env python3
from hclw.HCLW import HCLW
from hclw.Secret import Secret

from harpokrat_client_library.models import resource
from harpokrat_client_library.models.response import HarpokratResponse
from harpokrat_client_library.services import api_service
from harpokrat_client_library.services.auth_service import AuthService
from harpokrat_client_library.services.resource_service import ResourceService


class SecretService(ResourceService):
    def __init__(self, api_service: api_service, auth_service: AuthService, uri: str, wrapper: HCLW):
        super().__init__(api_service, '{}/secrets'.format(uri), 'secrets')
        self.wrapper = wrapper
        self.auth_service = auth_service

    def _secret_to_content(self, secret: Secret):
        if self.auth_service.key is None:
            raise
        return {'content': secret.get_raw_content(self.auth_service.key)}

    def _convert_data(self, resource: resource) -> resource:
        if resource.attributes and hasattr(resource.attributes, 'content'):
            secret = Secret(self.wrapper, self.auth_service.key, resource.attributes['content'])
            resource.attributes = secret
        return resource

    def create(self, attributes: Secret, relationships=None) -> HarpokratResponse:
        return super().create(self._secret_to_content(attributes), relationships)

    def read(self, resource_id: str) -> HarpokratResponse:
        response = super().read(resource_id)
        response.data = SecretService._convert_data(self, response.data)
        return response

    # TODO : temporary fix find a better wayy
    def filter_resource(self, resources):
        return filter(lambda x: x.relationships["owner"].data.id == self.auth_service.user_id, resources)

    def read_all(self) -> HarpokratResponse:
        response = super().read_all()
        response.data = self.filter_resource(response.data)
        response.data = [SecretService._convert_data(self, data) for data in response.data]
        return response

    def update(self, resource_id, attributes, relationships=None) -> HarpokratResponse:
        return super().update(resource_id, self._secret_to_content(attributes), relationships)

