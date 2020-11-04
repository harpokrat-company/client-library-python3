#!/usr/bin/env python3


class Group(dict):
    def __init__(self, name: str = None):
        super().__init__({
            'name': name,
        })
