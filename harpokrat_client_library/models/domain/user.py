#!/usr/bin/env python3


class User(dict):
    def __init__(self, email: str, password: str, first_name: str = None, last_name: str = None):
        super().__init__({
            'email': email,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
        })
