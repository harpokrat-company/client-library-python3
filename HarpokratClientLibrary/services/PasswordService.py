#!/usr/bin/env python3
import json

from hclw.HCLW import HCLW
from hclw.Secret import Secret

from HarpokratClientLibrary.models.HarpokratResponse import HarpokratResponse
from HarpokratClientLibrary.models.Resource import Resource
from HarpokratClientLibrary.models.domain.Password import Password
from HarpokratClientLibrary.services.ApiService import ApiService
from HarpokratClientLibrary.services.AuthService import AuthService
from HarpokratClientLibrary.services.SecretService import SecretService


class PasswordService(SecretService):
    def __init__(self, api_service: ApiService, auth_service: AuthService, uri: str, wrapper: HCLW):
        super().__init__(api_service, auth_service, uri, wrapper)

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

    def create(self, password, relationships=None) -> HarpokratResponse:
        return super().create(self._password_to_secret(password), relationships)

    def update(self, resource_id, password, relationships=None) -> HarpokratResponse:
        return super().update(resource_id, Secret(self.wrapper, json.dumps(password)))
