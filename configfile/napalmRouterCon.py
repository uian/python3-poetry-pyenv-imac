from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file='config.yaml')

def configure_router(task):
    driver = task.host.get('napalm_driver', 'huawei')#是华为的设备，ios应该改成huawei
    # optional_args = {'transport': 'telnet', 'port': 2000}
    with task.host.get_connection(driver) as conn:
        conn.open()
        device = conn.get_device()
        device.load_merge_candidate(config='interface Loopback0\nip address 10.0.1.1 255.255.255.0\nexit\n')
        diffs = device.compare_config()
        if len(diffs) > 0:
            device.commit_config()
            print(f"Configuration changes committed on {task.host.name}")
        else:
            print(f"No configuration changes needed on {task.host.name}")
        conn.close()
    result = task.run(task=napalm_configure, configuration={'protocols': {'ssh': {'enabled': True}}}, replace=False)
    print_result(result)

result = nr.run(task=configure_router)
print_result(result)
