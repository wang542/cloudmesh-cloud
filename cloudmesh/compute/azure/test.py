from cloudmesh.compute.azure import Provider as prv
from azure.cli.core import get_default_cli
import time
import json

# AZURE_CLI = 'az'
SERVICE_PRINCIPAL = 'cloudmesh'

cli = get_default_cli()


def get_az_account_list():
    cli.invoke(['account', 'list'])
    res = cli.result
    return res.result[0]


def az_login():
    cli.invoke(['login'])


def get_service_principal_credentials():
    cli.invoke(['ad', 'sp', 'create-for-rbac', '--name', SERVICE_PRINCIPAL])
    res = cli.result
    return res.result


account = {}
sp_cred = {}
# try:
#     account.update(get_az_account_list())
#
#     sp_cred.update(get_service_principal_credentials())
#     time.sleep(2)
#
#     # sleep for couple of seconds because it takes sometime
#     # to update the credentials
# except ValueError:
#     az_login()
#     account = get_az_account_list()

# print(account)
# print(sp_cred)
#
# cred = {
#     'AZURE_APPLICATION_ID': sp_cred['appId'],
#     'AZURE_SECRET_KEY': sp_cred['password'],
#     'AZURE_TENANT_ID': account['tenantId'],
#     'AZURE_SUBSCRIPTION_ID': account['id'],
# }
# print("Cred: " + str(cred))

p = prv.Provider()

# p.list()
# p.info()
# p.images()

# p.create()
# exit(0)

#
# exit(0)

# [print(r.__str__()) for r in p.list_public_ips()]

# print('####')
#
# print(p.find_available_public_ip().__str__())
#
# print('attach the ip to vm')
# print(p.attach_public_ip())

# print(p.create_public_ip())
# print(p.list_public_ips())
# print(p.delete_public_ip(ip='cloudmeshVM-pub-ip'))
# print(p.list_public_ips())

# p.add_secgroup(name='my_sec_group', description='aaaaa')
# [print(i.__str__()) for i in p.list_secgroups()]
# print('###', p.list_secgroups('test')[0].__str__())

# p.list_secgroup_rules()
# p.list_secgroups()
# p.list_secgroups('default')
# print(p.add_secgroup(name='test'))

# p.list_secgroup_rules()
# p.list_secgroup_rules('test')
# p.add_secgroup_rule(name='ssh2')

# p.add_secgroup('default')

# p.add_rules_to_secgroup('test', rules=['ssh', 'ssh2'])

# p.upload_secgroup('test')

p.destroy()

# out = p.info(name='test-niranda-vm-20')
# p.stop(name='test-niranda-vm-19')
pass
