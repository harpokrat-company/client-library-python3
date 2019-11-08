#!/usr/bin/env python3
from HarpokratClientLibrary.models.HarpokratObject import HarpokratObject


class JsonApi(HarpokratObject):
    version: str = None
    meta: str = None
