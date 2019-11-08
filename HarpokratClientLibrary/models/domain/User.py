#!/usr/bin/env python3
from typing import List

from HarpokratClientLibrary.models.HarpokratObject import HarpokratObject


class User(HarpokratObject):
    def __init__(self, email: str = None, password: str = None, first_name: str = None, last_name: str = None):
        super().__init__()
        self.email = email
        self.password = password
        self.firstName = first_name
        self.lastName = last_name
