#!/usr/bin/env python3
from harpokrat_client_library.api import Api


class RelationshipEndpoint:
    def __init__(self, api: Api, uri: str):
        self.api = api
        self.uri = uri

    def read(self):
        return self.api.get(self.uri)

    def add(self, attributes):
        return self.api.post(self.uri, data={'data': attributes})

    def set(self, attributes):
        return self.api.patch(self.uri, data={'data': attributes})

    def delete(self, attributes):
        return self.api.delete(self.uri, data={'data': attributes})
