#!/usr/bin/env python3

import requests

DEFAULT_TIMEOUT = 10


class ApiService:
    def __init__(self, auth_service):
        self.auth_service = auth_service

    def _get_request_headers(self, headers):
        if headers is None:
            headers = {}
        token = self.auth_service.token
        if token:
            headers['Authorization'] = 'Bearer {}'.format(token)
        return headers

    def get(self, url, params=None, headers=None):
        headers = self._get_request_headers(headers)
        response = requests.get(url, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        if response.status_code != 200:
            return None
        return response.json()

    def get_many(self, url, params=None, headers=None):
        return self.get(url, params=params, headers=headers)

    def post(self, url, data=None, params=None, headers=None):
        headers = self._get_request_headers(headers)
        response = requests.post(url, json=data, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        if response.status_code != 200:
            return None
        return response.json()

    def patch(self, url, data=None, params=None, headers=None):
        headers = self._get_request_headers(headers)
        response = requests.patch(url, json=data, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        if response.status_code != 200:
            return None
        return response.json()

    def put(self, url, data=None, params=None, headers=None):
        headers = self._get_request_headers(headers)
        response = requests.put(url, json=data, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        if response.status_code != 200:
            return None
        return response.json()

    def delete(self, url, params=None, headers=None):
        headers = self._get_request_headers(headers)
        response = requests.delete(url, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        if response.status_code != 200:
            return None
        return response.json()
