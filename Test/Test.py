#!/usr/bin/env python3
from hclw.Secret import Secret

from HarpokratClientLibrary.HarpokratAPI import HarpokratAPI
from HarpokratClientLibrary.models.domain.Password import Password
from HarpokratClientLibrary.models.domain.User import User

harpokrat_api = HarpokratAPI('https://api.harpokrat.com/v1')

test_user = User('aled.oskour2@gmail.com', 'aledoskour1234', 'jpp', 'flantier')

# response1 = harpokrat_api.user_service.create(test_user)
# print(response1)

response2 = harpokrat_api.token_service.login(test_user.email, test_user.password)
print(response2)

response3 = harpokrat_api.me_service.me()
print(response3)

pw = Password('flantier', 'aled', 'oskour', 'jpp')
response4 = harpokrat_api.user_password_service.create(pw)
print(response4)

pw_id = response4.data.id
response5 = harpokrat_api.password_service.read(pw_id)
print(response5)

response6 = harpokrat_api.user_password_service.read(pw_id)
print(response6)

response7 = harpokrat_api.user_password_service.read_all()
print(response7)

pw2 = Password('aled2', 'oskour2', 'jpp2')
response8 = harpokrat_api.user_password_service.update(pw_id, pw2)
print(response8)

harpokrat_api.password_service.delete(pw_id)
