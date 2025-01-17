#!/usr/bin/env python3
import requests
from requests import HTTPError

from harpokrat_client_library.exceptions import HarpokratHttpException

DEFAULT_TIMEOUT = 10


class Api:
    def __init__(self, auth):
        self.auth = auth

    def _get_request_headers(self, headers):
        if headers is None:
            headers = {}
        token = self.auth.token
        if token:
            headers['Authorization'] = 'Bearer {}'.format(token)
        return headers

    def get(self, url, params=None, headers=None):
        headers = self._get_request_headers(headers)
        try:
            response = requests.get(url, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
            response.raise_for_status()
        except HTTPError as error:
            raise HarpokratHttpException(error, url)
        if response.status_code != 200:
            return None
        return response.json()

    def get_many(self, url, params=None, headers=None):
        return self.get(url, params=params, headers=headers)

    def post(self, url, data=None, params=None, headers=None):
        headers = self._get_request_headers(headers)
        try:
            response = requests.post(url, json=data, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
            response.raise_for_status()
        except HTTPError as error:
            raise HarpokratHttpException(error, url, data)
        if response.status_code != 200:
            return None
        return response.json()

    def patch(self, url, data=None, params=None, headers=None):
        headers = self._get_request_headers(headers)
        try:
            response = requests.patch(url, json=data, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
            response.raise_for_status()
        except HTTPError as error:
            raise HarpokratHttpException(error, url, data)
        if response.status_code != 200:
            return None
        return response.json()

    def put(self, url, data=None, params=None, headers=None):
        headers = self._get_request_headers(headers)
        try:
            response = requests.put(url, json=data, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
            response.raise_for_status()
        except HTTPError as error:
            raise HarpokratHttpException(error, url, data)
        if response.status_code != 200:
            return None
        return response.json()

    def delete(self, url, data=None, params=None, headers=None):
        headers = self._get_request_headers(headers)
        try:
            response = requests.delete(url, json=data, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
            response.raise_for_status()
        except HTTPError as error:
            raise HarpokratHttpException(error, url, data)
        if response.status_code != 200:
            return None
        return response.json()
