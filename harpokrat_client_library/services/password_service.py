#!/usr/bin/env python3
from hclw.HCLW import HCLW

from harpokrat_client_library import convert
from harpokrat_client_library.models.relationship import Relationship
from harpokrat_client_library.models.resource_identifier import ResourceIdentifier
from harpokrat_client_library.authentication import Authentication
from harpokrat_client_library.endpoint.resource_endpoint import ResourceEndpoint


class PasswordService:
    def __init__(self, user_endpoint: ResourceEndpoint, secret_endpoint: ResourceEndpoint, wrapper: HCLW, auth: Authentication):
        self.user_endpoint = user_endpoint
        self.secret_endpoint = secret_endpoint
        self.wrapper = wrapper
        self.auth = auth

    def _convert_to_secret(self, data):
        return convert.password_to_secret(self.wrapper, self.auth.key, data)

    def _convert_to_password(self, data):
        return convert.secret_to_password(self.wrapper, self.auth.key, data)

    def read(self, resource_id: str):
        response = self.secret_endpoint.read(resource_id)
        owner_relationship = response['data']['relationships']['owner']['data']
        if owner_relationship['type'] != 'users' or owner_relationship['id'] != self.auth.user_id:
            raise Exception('invalid owner')
        response['data']['attributes'] = self._convert_to_password(response['data']['attributes'])
        return response

    def read_all(self):
        response = self.user_endpoint.resource(self.auth.user_id, 'secrets').read_all()
        for secret in response['data']:
            secret['attributes'] = self._convert_to_password(secret['attributes'])
        return response

    def create(self, attributes, relationships=None):
        if relationships is None:
            relationships = {}
        relationships['owner'] = Relationship(ResourceIdentifier('users', self.auth.user_id))
        return self.secret_endpoint.create(self._convert_to_secret(attributes), relationships)

    def update(self, resource_id, attributes, relationships=None):
        return self.secret_endpoint.update(resource_id, self._convert_to_secret(attributes), relationships)

    def delete(self, resource_id):
        return self.secret_endpoint.delete(resource_id)
