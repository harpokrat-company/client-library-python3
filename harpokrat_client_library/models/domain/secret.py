#!/usr/bin/env python3


class Secret(dict):
    def __init__(self, content: str, private: bool = True):
        super().__init__({
            'content': content,
            'private': private,
        })
