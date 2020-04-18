#!/usr/bin/env python3
from HarpokratClientLibrary.models.HarpokratObject import HarpokratObject


class Password(HarpokratObject):
    def __init__(self, name, login, password, domain):
        super().__init__()
        self.name = name
        self.login = login
        self.password = password
        self.domain = domain

    name: str
    login: str
    password: str
    domain: str
