#!/usr/bin/env python3

from harpokrat_client_library.harpokrat import Harpokrat
from harpokrat_client_library.models.domain.group import Group
from harpokrat_client_library.models.domain.organization import Organization
from harpokrat_client_library.models.domain.password import Password
from harpokrat_client_library.models.domain.user import User
from harpokrat_client_library.models.domain.vault import Vault
from harpokrat_client_library.models.relationship import Relationship
from harpokrat_client_library.models.resource_identifier import ResourceIdentifier


def title(text: str, indent=0):
    print('\033[1m\033[94m{}-> {}\033[0m'.format('\t'*indent, text))


hpk = Harpokrat('https://api.dev.harpokrat.com:443/v1')

test_user = User('pythonlib@osko.ur', 'testtest', 'jpp', 'flantier')

title('Login')
response = hpk.token_endpoint.login(test_user['email'], test_user['password'])
print(response)

title('Get Me')
response = hpk.me_service.read()
print(response)

#

title('Passwords')
title('Create password', 1)
pw = Password('flantier', 'aled', 'oskour', 'jpp', private=False)
response = hpk.password_service.create(pw)
print(response)
password_id = response['data']['id']

title('Get password', 1)
response = hpk.password_service.read(password_id)
print(response)

title('Get all passwords', 1)
hpk.password_service.read_all()

title('Update a password', 1)
pw2 = Password('flantier2', 'aled2', 'oskour2', 'jpp2')
hpk.password_service.update(password_id, pw2)

#

title('Organizations')

title('Create Organization', 1)
response = hpk.organization_endpoint.create(
    Organization('my coorp'),
    relationships={
        'owner': Relationship(ResourceIdentifier('users', hpk.auth.user_id))
    }
)
organization_id = response['data']['id']
print(response)


title('List Organizations', 1)
response = hpk.organization_endpoint.read_all()
print(response)

title('Get Organization', 1)
response = hpk.organization_endpoint.read(organization_id)
print(response)

title('Update Organization', 1)
response = hpk.organization_endpoint.update(
    organization_id,
    {'name': 'my new coorp'}
)
print(response)

title('Organization Members', 1)
title('Add Organization Member', 2)
response = hpk.organization_endpoint.relationship(organization_id, 'members').add(
    [ResourceIdentifier('users', hpk.auth.user_id)]
)
print(response)
title('Get Organization Members Relationship', 2)
response = hpk.organization_endpoint.relationship(organization_id, 'members').read()
print(response)
title('Get Organization Members Resource', 2)
response = hpk.organization_endpoint.resource(organization_id, 'members').read()
print(response)

title('Organization Groups', 1)
title('Get Organization Groups Relationship', 2)
response = hpk.organization_endpoint.relationship(organization_id, 'groups').read()
print(response)
title('Get Organization Groups Resource', 2)
response = hpk.organization_endpoint.resource(organization_id, 'groups').read()
print(response)

title('Organization Owner', 1)
title('Get Organization Owner Relationship', 2)
response = hpk.organization_endpoint.relationship(organization_id, 'owner').read()
print(response)
title('Get Organization Owner Resource', 2)
response = hpk.organization_endpoint.resource(organization_id, 'owner').read()
print(response)

#

title('Groups')
title('Create Group', 1)
response = hpk.group_endpoint.create(
    Group('my group'),
    relationships={
        'organization': Relationship(ResourceIdentifier('organizations', organization_id))
    }
)
print(response)
group_id = response['data']['id']

title('Create a child group', 1)
response = hpk.group_endpoint.create(
    Group('my group bis'),
    relationships={
        'organization': Relationship(ResourceIdentifier('organizations', organization_id)),
        'parent': Relationship(ResourceIdentifier('groups', group_id))
    }
)
print(response)
group_child_id = response['data']['id']

title('List Groups', 1)
response = hpk.group_endpoint.read_all()
print(response)

title('Get Group', 1)
response = hpk.group_endpoint.read(group_id)
print(response)

title('Update Group', 1)
response = hpk.group_endpoint.update(
    group_id,
    {'name': 'my new group'}
)
print(response)

title('Group Members', 1)
title('Add User To Group', 2)
response = hpk.group_endpoint.relationship(group_id, 'members').add(
    [ResourceIdentifier('users', hpk.auth.user_id)]
)
print(response)
title('Get Group Members Relationship', 2)
response = hpk.group_endpoint.relationship(group_id, 'members').read()
print(response)
title('Get Group Members Resource', 2)
response = hpk.group_endpoint.resource(group_id, 'members').read()
print(response)

title('Group Parent', 1)
title('Get Group Parent Relationship', 2)
response = hpk.group_endpoint.relationship(group_id, 'parent').read()
print(response)
title('Get Group Parent Resource', 2)
response = hpk.group_endpoint.resource(group_id, 'parent').read()
print(response)

title('Group Children', 1)
title('Get Group Children Relationship', 2)
response = hpk.group_endpoint.relationship(group_id, 'children').read()
print(response)
title('Get Group Children Resource', 2)
response = hpk.group_endpoint.resource(group_id, 'children').read()
print(response)

title('Group Secrets', 1)
# TODO : Group Secrets

title('Group Organization', 1)
title('Get Group Organization Relationship', 2)
response = hpk.group_endpoint.relationship(group_id, 'organization').read()
print(response)
title('Get Group Organization Resource', 2)
response = hpk.group_endpoint.resource(group_id, 'organization').read()
print(response)

title('Group Vaults', 1)
title('Get Group Vaults Relationship', 2)
response = hpk.group_endpoint.relationship(group_id, 'vaults').read()
print(response)
title('Get Group Vaults Resource', 2)
response = hpk.group_endpoint.resource(group_id, 'vaults').read()
print(response)

#

title('Vaults')
title('Create Vault in Organization', 1)
response = hpk.vault_endpoint.create(
    Vault('my vault'),
    relationships={
        'owner': Relationship(ResourceIdentifier('groups', group_id))
    }
)
print(response)
vault_group_id = response['data']['id']

title('Create Vault in User', 1)
response = hpk.vault_endpoint.create(
    Vault('my vault'),
    relationships={
        'owner': Relationship(ResourceIdentifier('users', hpk.auth.user_id))
    }
)
print(response)
vault_user_id = response['data']['id']

title('List Vaults', 1)
response = hpk.vault_endpoint.read_all()
print(response)

title('Get Vault')
response = hpk.vault_endpoint.read(vault_group_id)
print(response)

title('Update Vault', 1)
response = hpk.vault_endpoint.update(
    vault_group_id,
    {'name': 'my new vault'}
)
print(response)

title('Vault Owner', 1)
title('Get Vault Owner Group Relationship', 2)
response = hpk.vault_endpoint.relationship(vault_group_id, 'owner').read()
print(response)
title('Get Vault Owner Group Resource', 2)
response = hpk.vault_endpoint.resource(vault_group_id, 'owner').read()
print(response)
title('Get Vault Owner User Relationship', 2)
response = hpk.vault_endpoint.relationship(vault_user_id, 'owner').read()
print(response)
title('Get Vault Owner User Resource', 2)
response = hpk.vault_endpoint.resource(vault_user_id, 'owner').read()
print(response)

title('Vault Secrets', 1)
# TODO : vault secrets

#

title('User')
title('Get User', 1)
response = hpk.user_endpoint.read(hpk.auth.user_id)
print(response)

title('Get Owned Organizations Relationship', 1)
response = hpk.user_endpoint.relationship(hpk.auth.user_id, 'ownedOrganizations').read()
print(response)
title('Get Owned Organizations Resource', 1)
response = hpk.user_endpoint.resource(hpk.auth.user_id, 'ownedOrganizations').read()
print(response)

title('Get Organizations Relationship', 1)
response = hpk.user_endpoint.relationship(hpk.auth.user_id, 'organizations').read()
print(response)
title('Get Organizations Resource', 1)
response = hpk.user_endpoint.resource(hpk.auth.user_id, 'organizations').read()
print(response)

title('Get Vaults Relationship', 1)
response = hpk.user_endpoint.relationship(hpk.auth.user_id, 'vaults').read()
print(response)
title('Get Vaults Resource', 1)
response = hpk.user_endpoint.resource(hpk.auth.user_id, 'vaults').read()
print(response)

title('Get Logs Relationship', 1)
response = hpk.user_endpoint.relationship(hpk.auth.user_id, 'logs').read()
print(response)
title('Get Logs Resource', 1)
response = hpk.user_endpoint.resource(hpk.auth.user_id, 'logs').read()
print(response)

#

title('Delete All')
title('Delete vault group', 1)
hpk.vault_endpoint.delete(vault_group_id)
title('Delete vault user', 1)
hpk.vault_endpoint.delete(vault_user_id)
title('Delete child group', 1)
hpk.group_endpoint.delete(group_child_id)
title('Delete member from group', 1)
hpk.group_endpoint.relationship(group_id, 'members').delete([ResourceIdentifier('users', hpk.auth.user_id)])
title('Delete group', 1)
hpk.group_endpoint.delete(group_id)
title('Delete member from organization', 1)
hpk.organization_endpoint.relationship(organization_id, 'members').delete([ResourceIdentifier('users', hpk.auth.user_id)])
title('Delete organization', 1)
hpk.organization_endpoint.delete(organization_id)
title('Delete password', 1)
hpk.password_service.delete(password_id)
