#!/usr/bin/env python3
import random

from HarpokratClientLibrary.HarpokratAPI import HarpokratAPI
from HarpokratClientLibrary.models.Resource import Resource
from HarpokratClientLibrary.models.domain.User import User

harpokrat_api = HarpokratAPI('https://api.harpokrat.com/v1')

test_user = User('aled.oskour{}@gmail.com'.format(random.randint(0, 1000)), 'aledoskour1234', 'jpp', 'flantier')
test_resource = Resource(test_user, 'users')

response1 = harpokrat_api.user_service.create(test_user)
print(response1)

response2 = harpokrat_api.token_service.login(test_user.email, test_user.password)
print(response2)
