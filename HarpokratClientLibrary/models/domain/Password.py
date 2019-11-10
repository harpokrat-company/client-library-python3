#!/usr/bin/env python3
from HarpokratClientLibrary.models.HarpokratObject import HarpokratObject


class Password(HarpokratObject):
    def __init__(self, login=None, password=None, domain=None):
        super().__init__()
        self.login = login
        self.password = password
        self.domain = domain

    login: str
    password: str
    domain: str
