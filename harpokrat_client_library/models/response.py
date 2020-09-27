#!/usr/bin/env python3
from typing import List, Union

import six

from harpokrat_client_library.models.error import Error
from harpokrat_client_library.models.object import HarpokratObject, convert_to_harpokrat_object
from harpokrat_client_library.models.json_api import JsonApi
from harpokrat_client_library.models.resource import Resource


class HarpokratResponse(HarpokratObject):
    def refresh_from(self, values):
        for key, value in six.iteritems(values.copy()):
            self.__setitem__(key, convert_to_harpokrat_object(key, value, types={
                'data': Resource,
                'jsonapi': JsonApi,
                'errors': Error
            }))

    data: Union[Resource, List[Resource]]
    jsonapi: JsonApi
    Error: List[Error]
