#!/usr/bin/env python3
from typing import Dict

import six

from harpokrat_client_library.models.object import HarpokratObject, convert_to_harpokrat_object
from harpokrat_client_library.models.link import Link
from harpokrat_client_library.models.resource_identifier import ResourceIdentifier


class Relationship(HarpokratObject):

    def __init__(self, data=None, links=None, meta=None):
        super().__init__()
        self.links = links
        self.data = data
        self.meta = meta

    def refresh_from(self, values):
        for key, value in six.iteritems(values.copy()):
            self.__setitem__(key, convert_to_harpokrat_object(key, value, types={
                'data': ResourceIdentifier
            }))

    data: ResourceIdentifier
    meta: str
    links: Dict[str, Link]
