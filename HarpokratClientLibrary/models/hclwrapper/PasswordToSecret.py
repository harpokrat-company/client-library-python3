#!/usr/bin/env python3
import base64
import binascii
import json
from json import JSONDecodeError
from typing import Union

from HarpokratClientLibrary.models.domain.Password import Password
from HarpokratClientLibrary.models.domain.Secret import Secret


def password_from_secret(secret: Secret) -> Union[Password, None]:
    try:
        content = json.loads(base64.b64decode(secret.content.encode('utf-8')).decode('utf-8'))
        return Password.construct_from(content)
    except (binascii.Error, JSONDecodeError):
        return None


def secret_from_password(password: Password) -> Secret:
    content = base64.b64encode(json.dumps(password).encode('utf-8')).decode('utf-8')
    return Secret(content)
