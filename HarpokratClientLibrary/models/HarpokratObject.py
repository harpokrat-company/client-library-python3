#!/usr/bin/env python3

import six


def convert_to_harpokrat_object(name, data, types=None, special_types=None, plural_dicts_types=None):
    if types is None:
        types = {}
    if special_types is None:
        special_types = {}
    if plural_dicts_types is None:
        plural_dicts_types = {}

    if isinstance(data, list):
        return [convert_to_harpokrat_object(name, x) for x in data]

    if name in plural_dicts_types:
        return {key: convert_to_harpokrat_object(plural_dicts_types.get(name), data[key]) for key in data}

    if name in special_types:
        obj = special_types.get(name)
        return obj.construct_from(data)

    if isinstance(data, dict) and name in types:
        obj = types.get(name)
        return obj.construct_from(data)

    return data


class HarpokratObject(dict):
    def __setattr__(self, name, value):
        if name[0] == '_' or name in self.__dict__:
            return super(HarpokratObject, self).__setattr__(name, value)

        self[name] = value

    def __getattr__(self, name):
        return self[name]

    def __delattr__(self, name):
        if name[0] == '_':
            return super(HarpokratObject, self).__delattr__(name)

        del self[name]

    def __setitem__(self, key, value):
        key = key.lstrip('_')
        super(HarpokratObject, self).__setitem__(key, value)

    @classmethod
    def construct_from(cls, values):
        instance = cls()
        instance.refresh_from(values)
        return instance

    def refresh_from(self, values):
        for key, value in six.iteritems(values.copy()):
            self.__setitem__(key, convert_to_harpokrat_object(key, value))

