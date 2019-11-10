#!/usr/bin/env python3
from HarpokratClientLibrary.models.HarpokratObject import HarpokratObject


class Secret(HarpokratObject):
    def __init__(self, content: str = None):
        super().__init__()
        self.content = content
