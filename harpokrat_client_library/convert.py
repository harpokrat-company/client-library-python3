#!/usr/bin/env python3
from hclw.HCLW import HCLW
from hclw.Secret import Secret as HCLWSecret

from harpokrat_client_library.models.domain.password import Password
from harpokrat_client_library.models.domain.secret import Secret


def password_to_secret(wrapper: HCLW, key: str, password) -> Secret:
    secret = HCLWSecret(wrapper, key)
    secret.name = password['name']
    secret.login = password['login']
    secret.password = password['password']
    secret.domain = password['domain']
    return Secret(secret.get_raw_content(key), password['private'])


def secret_to_password(wrapper: HCLW, key: str, secret):
    return Password.create_from_secret(
        HCLWSecret(wrapper, key=key, content=secret['content']),
        secret['private']
    )
