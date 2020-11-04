#!/usr/bin/env python3


class Vault(dict):
    def __init__(self, name: str = None):
        super().__init__({
            'name': name,
        })
