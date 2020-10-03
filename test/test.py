#!/usr/bin/env python3

from harpokrat_client_library.harpokrat import Harpokrat
from harpokrat_client_library.models.domain.password import Password
from harpokrat_client_library.models.domain.user import User

hpk = Harpokrat('https://api.dev.harpokrat.com:443/v1')

test_user = User('pythonlib@osko.ur', 'testtest', 'jpp', 'flantier')

print('-> Login')
response = hpk.token_endpoint.login(test_user['email'], test_user['password'])
print(response)

print('-> Get User')
response = hpk.me_service.read()
print(response)

print('-> Create password')
pw = Password('flantier', 'aled', 'oskour', 'jpp', private=False)
response = hpk.password_service.create(pw)
pw_id = response['data']['id']
print(response)

print('-> Get password')
response = hpk.password_service.read(pw_id)
print(response)

print('-> Get all passwords')
response = hpk.password_service.read_all()
print(response)

print('-> Update a password')
pw2 = Password('flantier2', 'aled2', 'oskour2', 'jpp2')
response = hpk.password_service.update(pw_id, pw2)
print(response)

print('-> Delete password')
response = hpk.password_service.delete(pw_id)
print(response)
