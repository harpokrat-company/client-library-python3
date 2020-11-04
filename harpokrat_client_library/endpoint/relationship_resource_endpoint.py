#!/usr/bin/env python3
from harpokrat_client_library.api import Api


class RelationshipResourceEndpoint:
    def __init__(self, api: Api, uri: str):
        self.api = api
        self.uri = uri

    def read(self):
        return self.api.get(self.uri)
