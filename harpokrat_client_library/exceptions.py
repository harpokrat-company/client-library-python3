#!/usr/bin/env python3


class HarpokratException(Exception):
    pass


class HarpokratHttpException(HarpokratException):
    def __init__(self, error, url):
        self.error = error
        self.url = url
