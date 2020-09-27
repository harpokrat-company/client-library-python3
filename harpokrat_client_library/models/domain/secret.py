#!/usr/bin/env python3
from harpokrat_client_library.models.object import HarpokratObject


class Secret(HarpokratObject):
    def __init__(self, content: str = None):
        super().__init__()
        self.content = content
