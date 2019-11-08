#!/usr/bin/env python3
from typing import List

import six
from HarpokratClientLibrary.models.HarpokratObject import HarpokratObject


class Relationship(HarpokratObject):

    def __init__(self, links, data, meta):
        super().__init__()
        self.links = links
        self.data = data
        self.meta = meta



