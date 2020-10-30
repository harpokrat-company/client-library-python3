#!/usr/bin/env python3
from harpokrat_client_library.authentication import Authentication
from harpokrat_client_library.endpoint.user_endpoint import UserEndpoint


class MeService:
    def __init__(self, auth: Authentication, user_endpoint: UserEndpoint):
        self.auth = auth
        self.user_endpoint = user_endpoint

    def resource(self, resource_name: str):
        if self.auth.user_id is None:
            raise Exception('no user authenticated')
        return self.user_endpoint.resource(self.auth.user_id, resource_name)

    def relationship(self, resource_name: str):
        if self.auth.user_id is None:
            raise Exception('no user authenticated')
        return self.user_endpoint.relationship(self.auth.user_id, resource_name)

    def read(self):
        if self.auth.user_id is None:
            raise Exception('no user authenticated')
        return self.user_endpoint.read(self.auth.user_id)
