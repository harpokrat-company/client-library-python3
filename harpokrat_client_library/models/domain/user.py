#!/usr/bin/env python3

from harpokrat_client_library.models.object import HarpokratObject


class User(HarpokratObject):
    def __init__(self, email: str = None, password: str = None, first_name: str = None, last_name: str = None):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
