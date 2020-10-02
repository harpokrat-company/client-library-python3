#!/usr/bin/env python3

from harpokrat_client_library.services.api_service import ApiService


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

    def read(self, resource_id: str) -> dict:
        response = self.api.get(self._build_url(resource_id))
        return response

    def read_all(self) -> dict:
        response = self.api.get_many(self.uri)
        return response

    def create(self, attributes, relationships=None) -> dict:
        resource = {
            'attributes': attributes,
            'type': self.resource_type,
            'relationships': relationships
        }
        response = self.api.post(self.uri, data={'data': resource})
        return response

    def update(self, resource_id, attributes, relationships=None) -> dict:
        resource = {
            'attributes': attributes,
            'type': self.resource_type,
            'relationships': relationships,
            'id': resource_id
        }
        response = self.api.patch(self._build_url(resource_id), data={'data': resource})
        return response

    def delete(self, resource_id) -> dict:
        response = self.api.delete(self._build_url(resource_id))
        return response
