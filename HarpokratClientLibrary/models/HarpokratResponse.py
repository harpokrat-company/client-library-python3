#!/usr/bin/env python3
import six

from HarpokratClientLibrary.models.Error import Error
from HarpokratClientLibrary.models.HarpokratObject import HarpokratObject, convert_to_harpokrat_object
from HarpokratClientLibrary.models.JsonApi import JsonApi
from HarpokratClientLibrary.models.Resource import Resource


class HarpokratResponse(HarpokratObject):
    def refresh_from(self, values):
        for key, value in six.iteritems(values.copy()):
            self.__setitem__(key, convert_to_harpokrat_object(key, value, types={
                'data': Resource,
                'jsonapi': JsonApi,
                'errors': Error
            }))
