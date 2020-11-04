#!/usr/bin/env python3

from harpokrat_client_library.api import Api
from harpokrat_client_library.endpoint.relationship_endpoint import RelationshipEndpoint
from harpokrat_client_library.endpoint.relationship_resource_endpoint import RelationshipResourceEndpoint


class ResourceEndpoint:
    def __init__(self, api: Api, uri: str, resource_type: str = None):
        self.api = api
        self.uri = uri
        self.resource_type = resource_type

    def _resolve_path(self, *args: [str]):
        return '/'.join([self.uri, *args])

    def resource(self, resource_id: str, resource_name: str) -> RelationshipResourceEndpoint:
        return RelationshipResourceEndpoint(
            self.api,
            self._resolve_path(resource_id, resource_name)
        )

    def relationship(self, resource_id: str, resource_name: str) -> RelationshipEndpoint:
        return RelationshipEndpoint(
            self.api,
            self._resolve_path(resource_id, 'relationships', resource_name)
        )

    def read(self, resource_id: str):
        response = self.api.get(self._resolve_path(resource_id))
        return response

    def read_all(self):
        response = self.api.get_many(self.uri)
        return response

    def create(self, attributes, relationships=None):
        resource = {
            'attributes': attributes,
            'type': self.resource_type,
            'relationships': relationships
        }
        response = self.api.post(self.uri, data={'data': resource})
        return response

    def update(self, resource_id, attributes, relationships=None):
        resource = {
            'attributes': attributes,
            'type': self.resource_type,
            'relationships': relationships,
            'id': resource_id
        }
        response = self.api.patch(self._resolve_path(resource_id), data={'data': resource})
        return response

    def delete(self, resource_id):
        response = self.api.delete(self._resolve_path(resource_id))
        return response
