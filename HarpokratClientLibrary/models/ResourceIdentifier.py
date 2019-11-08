#!/usr/bin/env python3
from typing import List

from HarpokratClientLibrary.models.HarpokratObject import HarpokratObject


class ResourceIdentifier(HarpokratObject):
    def __init__(self, type: str, id=None, meta=None):
        super().__init__()
        self.type = type
        self.id = id
        self.meta = meta


