#!/usr/bin/env python3
from typing import Dict

import six

from harpokrat_client_library.models.object import convert_to_harpokrat_object
from harpokrat_client_library.models.relationship import Relationship
from harpokrat_client_library.models.resource_identifier import ResourceIdentifier
from harpokrat_client_library.models.domain.json_web_token import JsonWebToken
from harpokrat_client_library.models.domain.secret import Secret
from harpokrat_client_library.models.domain.user import User


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

