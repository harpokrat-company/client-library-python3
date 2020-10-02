#!/usr/bin/env python3

from harpokrat_client_library.models.resource_identifier import ResourceIdentifier


class Relationship(dict):
    def __init__(self, data: ResourceIdentifier = None, meta: str = None):
        super().__init__({
            'data': data,
            'meta': meta
        })
