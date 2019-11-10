#!/usr/bin/env python3

from HarpokratClientLibrary.models.HarpokratResponse import HarpokratResponse
from HarpokratClientLibrary.models.Resource import Resource
from HarpokratClientLibrary.services import ApiService


class ResourceService:
    def __init__(self, api_service: ApiService, uri: str, resource_type: str = None):
        self.api = api_service
        self.uri = uri
        self.resource_type = resource_type

    def _build_url(self, path) -> str:
        url = self.uri
        if url.endswith('/'):
            url = url[:-1]
        if url.startswith('/'):
            url = url[1:]
        return url + '/' + path

    def read(self, resource_id: str) -> HarpokratResponse:
        response = self.api.get(self._build_url(resource_id))
        return HarpokratResponse.construct_from(response)

    def read_all(self) -> HarpokratResponse:
        response = self.api.get_many(self.uri)
        return HarpokratResponse.construct_from(response)

    def create(self, attributes, relationships=None) -> HarpokratResponse:
        resource = Resource(attributes, self.resource_type, relationships)
        response = self.api.post(self.uri, data={'data': resource})
        return HarpokratResponse.construct_from(response)

    def update(self, resource_id, attributes, relationships=None) -> HarpokratResponse:
        resource = Resource(attributes, self.resource_type, relationships)
        response = self.api.patch(self._build_url(resource_id), data={'data': resource})
        return HarpokratResponse.construct_from(response)

    def delete(self, resource_id) -> None:
        self.api.delete(self._build_url(resource_id))
