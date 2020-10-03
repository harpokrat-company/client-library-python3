#!/usr/bin/env python3


class ResourceIdentifier(dict):
    def __init__(self, type: str, id: str = None, meta=None):
        super().__init__({
            'type': type,
            'id': id,
            'meta': meta
        })
