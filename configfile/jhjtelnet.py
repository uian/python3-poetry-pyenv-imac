from nornir import InitNornir
from nornir_scrapli.tasks import send_configs

nr = InitNornir(config_file="config.yaml")

interface_range = "GigabitEthernet0/0/1-5"
lacp_mode = "lacp-static"
aggregated_interface = "eth-trunk1"

config = [
    f"interface range {interface_range}",
    f"lacp mode {lacp_mode}",
    f"ethernet eth-trunk {aggregated_interface}",
]

results = nr.run(task=send_configs, configs=config)
