#!/usr/bin/env python3
from HarpokratClientLibrary.models.HarpokratObject import HarpokratObject


class Link(HarpokratObject):
    href: str
    meta: str

