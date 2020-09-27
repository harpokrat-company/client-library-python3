#!/usr/bin/env python3
from harpokrat_client_library.models.object import HarpokratObject


class Link(HarpokratObject):
    href: str
    meta: str
