#!/usr/bin/env python3
from typing import Dict

import six

from HarpokratClientLibrary.models.HarpokratObject import convert_to_harpokrat_object
from HarpokratClientLibrary.models.Relationship import Relationship
from HarpokratClientLibrary.models.ResourceIdentifier import ResourceIdentifier
from HarpokratClientLibrary.models.domain.JsonWebToken import JsonWebToken
from HarpokratClientLibrary.models.domain.Secret import Secret
from HarpokratClientLibrary.models.domain.User import User


class Resource(ResourceIdentifier):
    def __init__(self, attributes=None, resource_type: str = None, relationships=None, id=None):
        super().__init__(resource_type, id)
        self.attributes = attributes
        self.relationships = relationships

    def refresh_from(self, values):
        available_resources = {
            'json-web-tokens': JsonWebToken,
            'users': User,
            'secrets': Secret
        }
        self.type = convert_to_harpokrat_object('type', values['type'])
        types = {'attributes': available_resources.get(self.type)} if self.type else {}
        for key, value in six.iteritems(values.copy()):
            self.__setitem__(key, convert_to_harpokrat_object(key, value, types=types, plural_dicts_types={
                'relationships': Relationship
            }))

    attributes: object
    relationships: Dict

