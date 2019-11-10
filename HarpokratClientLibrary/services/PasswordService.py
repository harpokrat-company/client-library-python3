#!/usr/bin/env python3
from HarpokratClientLibrary.models.HarpokratResponse import HarpokratResponse
from HarpokratClientLibrary.models.Resource import Resource
from HarpokratClientLibrary.models.hclwrapper.PasswordToSecret import password_from_secret, secret_from_password
from HarpokratClientLibrary.services.ApiService import ApiService
from HarpokratClientLibrary.services.SecretService import SecretService


class PasswordService(SecretService):
    def __init__(self, api_service: ApiService, uri: str):
        super().__init__(api_service, uri)

    @staticmethod
    def _password_from_secret(data: Resource):
        if data.attributes:
            data.attributes = password_from_secret(data.attributes)
        return data

    def read(self, resource_id: str) -> HarpokratResponse:
        response = super().read(resource_id)
        response.data = self._password_from_secret(response.data)
        return response

    def read_all(self) -> HarpokratResponse:
        response = super().read_all()
        response.data = [self._password_from_secret(data) for data in response.data]
        return response

    def create(self, password, relationships=None) -> HarpokratResponse:
        return super().create(secret_from_password(password), relationships)

    def update(self, resource_id, password, relationships=None) -> HarpokratResponse:
        return super().update(resource_id, secret_from_password(password))
