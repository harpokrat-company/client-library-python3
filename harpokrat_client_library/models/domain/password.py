#!/usr/bin/env python3
from hclw.Secret import Secret


class Password(dict):
    def __init__(self, name: str = None, login: str = None, password: str = None, domain: str = None, private: bool = True):
        super().__init__({
            'name': name,
            'login': login,
            'password': password,
            'domain': domain,
            'private': private
        })

    @staticmethod
    def create_from_secret(secret: Secret, private: bool = True):
        return Password(secret.name, secret.login, secret.password, secret.domain, private)
