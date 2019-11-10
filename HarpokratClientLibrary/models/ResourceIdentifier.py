#!/usr/bin/env python3

from HarpokratClientLibrary.models.HarpokratObject import HarpokratObject


class ResourceIdentifier(HarpokratObject):
    def __init__(self, type=None, id=None, meta=None):
        super().__init__()
        self.type = type
        self.id = id
        self.meta = meta

    type: str
    id: str
    meta: str
