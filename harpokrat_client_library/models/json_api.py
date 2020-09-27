#!/usr/bin/env python3
from harpokrat_client_library.models.object import HarpokratObject


class JsonApi(HarpokratObject):
    version: str = None
    meta: str = None
