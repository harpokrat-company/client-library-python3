#!/usr/bin/env python3
from hclw.Secret import Secret

from harpokrat_client_library.api import HarpokratAPI
from harpokrat_client_library.models.domain.password import Password
from harpokrat_client_library.models.domain.user import User

harpokrat_api = HarpokratAPI('https://api.dev.harpokrat.com/v1')

test_user = User('louis.mallez@epitech.eu', 'toto1234', 'jpp', 'flantier')

# print('-> Create User')
# response1 = harpokrat_api.user_service.create(test_user)
# print(response1)

print('-> Login')
response2 = harpokrat_api.token_service.login(test_user.email, test_user.password)
print(response2)

response3 = harpokrat_api.me_service.me()
print(response3)

print('-> Create password')
pw = Password('flantier', 'aled', 'oskour', 'jpp')
response4 = harpokrat_api.user_password_service.create(pw)
print(response4)

print('-> Get password')
pw_id = response4.data.id
response5 = harpokrat_api.user_password_service.read(pw_id)
print(response5)

print('-> Get all passwords')
response7 = harpokrat_api.user_password_service.read_all()
print(response7)

print('-> Update a password')
pw2 = Password('flantier2', 'aled2', 'oskour2', 'jpp2')
response8 = harpokrat_api.user_password_service.update(pw_id, pw2)
print(response8)

print('-> Delete password')
harpokrat_api.password_service.delete(pw_id)
