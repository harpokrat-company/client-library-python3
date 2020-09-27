#!/usr/bin/env python3
from hclw.Secret import Secret

from harpokrat_client_library.models.domain.password import Password
from harpokrat_client_library.models.resource import Resource
from harpokrat_client_library.models.response import HarpokratResponse
from harpokrat_client_library.services.secret_service import SecretService


class PasswordService(SecretService):
    def _password_to_secret(self, password: Password) -> Secret:
        secret = Secret(self.wrapper, "")
        secret.name = password.name
        secret.login = password.login
        secret.password = password.password
        secret.domain = password.domain
        return secret

    def _convert_data(self, data: Resource) -> Resource:
        if data.attributes:
            secret = data.attributes
            password = Password(secret.name, secret.login, secret.password, secret.domain)
            data.attributes = password
        return data

    def read(self, resource_id: str) -> HarpokratResponse:
        response = super().read(resource_id)
        response.data = PasswordService._convert_data(self, response.data)
        return response

    def read_all(self) -> HarpokratResponse:
        response = super().read_all()
        response.data = [PasswordService._convert_data(self, data) for data in response.data]
        return response

    def create(self, attributes, relationships=None) -> HarpokratResponse:
        return super().create(self._password_to_secret(attributes), relationships)

    def update(self, resource_id, attributes, relationships=None) -> HarpokratResponse:
        return super().update(resource_id, self._password_to_secret(attributes))
