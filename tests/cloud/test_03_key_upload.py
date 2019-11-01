###############################################################
# pytest -v --capture=no tests/cloud/test_01_key.py
# pytest -v  tests/cloud/test_01_key.py
###############################################################
from pprint import pprint

import pytest
from cloudmesh.common.util import HEADING
from cloudmesh.common.variables import Variables
from cloudmesh.common3.Benchmark import Benchmark
from cloudmesh.compute.vm.Provider import Provider
from cloudmesh.configuration.Config import Config
from cloudmesh.key.Key import Key
from cloudmesh.mongo.CmDatabase import CmDatabase

Benchmark.debug()

user = Config()["cloudmesh.profile.user"]
variables = Variables()
KEY = f'{user}-key'
variables['key'] = KEY

cloud = variables.parameter('cloud')

print(f"Test run for {cloud}")

if cloud is None:
    raise ValueError("cloud is not not set")

cm = CmDatabase()
provider = Provider(name=cloud)


@pytest.mark.skip(reason="These have already been tested in test_02")
class Test_Key:

    def test_cleanup(self):
        HEADING()
        cm.clear(collection=f"local-key")
        try:
            r = provider.key_delete(KEY)
        except:
            pass

    def test_upload_key_to_database(self):
        HEADING()
        local = Key()
        pprint(local)
        Benchmark.Start()
        local.add(KEY, "ssh")
        Benchmark.Stop()

        key = cm.find_name(KEY, "key")[0]
        key['name'] == KEY

    def test_upload_key_to_cloud(self):
        HEADING()

        if cloud == 'azure':
            # todo: implement this
            return

        if cloud == 'aws':
            all_keys = cm.find_all_by_name(KEY, "key")
            for k in all_keys:
                if 'public_key' in k.keys():
                    key = k
                    break
        else:
            key = cm.find_name(KEY, "key")[0]
        pprint(key)
        Benchmark.Start()
        r = provider.key_upload(key)
        Benchmark.Stop()
        # print ("PPP", r)

    def test_list_key_from_cloud(self):
        HEADING()

        if cloud == 'azure':
            # todo: implement this
            return

        Benchmark.Start()
        keys = provider.keys()
        Benchmark.Stop()
        found = False
        for key in keys:
            if key['name'] == KEY:
                found = True
                break
        assert found

    def test_benchmark(self):
        Benchmark.print(sysinfo=False, csv=True, tag=cloud)
