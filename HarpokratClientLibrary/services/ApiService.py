#!/usr/bin/env python3

import requests
from requests import Response

DEFAULT_TIMEOUT = 10


class ApiService:
    def __init__(self, auth_service):
        self.auth_service = auth_service

    def _get_request_headers(self, headers):
        token = self.auth_service.token
        if token:
            headers['Authorization'] = token

        return headers

    def get(self, url, params=None, json=True, headers=None) -> Response:
        headers = self._get_request_headers(headers)
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        if json:
            response.json()
        else:
            return response

    def get_many(self, url, params=None, json=True, headers=None) -> [Response]:
        return self.get(url, params=params, json=json, headers=headers)

    def post(self, url, data=None, params=None, headers=None) -> Response:
        headers = self._get_request_headers(headers)
        response = requests.post(url, json=data, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()

    def patch(self, url, data=None, params=None, headers=None) -> Response:
        headers = self._get_request_headers(headers)
        response = requests.put(url, json=data, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()

    def put(self, url, data=None, params=None, headers=None) -> Response:
        headers = self._get_request_headers(headers)
        response = requests.put(url, json=data, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()

    def delete(self, url, params=None, headers=None) -> Response:
        headers = self._get_request_headers(headers)
        response = requests.delete(url, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()
