#!/usr/bin/env python3
from harpokrat_client_library import convert
from harpokrat_client_library.services.secret_service import SecretService


class PasswordService(SecretService):
    def _convert_to_secret(self, data):
        return convert.password_to_secret(self.wrapper, self.auth_service.key, data)

    def _convert_to_password(self, data):
        return convert.secret_to_password(self.wrapper, self.auth_service.key, data)

    def read(self, resource_id: str):
        response = super().read(resource_id)
        response['data']['attributes'] = self._convert_to_password(response['data']['attributes'])
        return response

    def read_all(self):
        response = super().read_all()
        for secret in response['data']:
            secret['attributes'] = self._convert_to_password(secret['attributes'])
        return response

    def create(self, attributes, relationships=None):
        return super().create(self._convert_to_secret(attributes), relationships)

    def update(self, resource_id, attributes, relationships=None):
        return super().update(resource_id, self._convert_to_secret(attributes))
