from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result

import os

files_and_folders = os.listdir() # 获得当前目录下的文件和文件夹
print(files_and_folders) 


nr = InitNornir(config_file="config.yaml")

def configure_router(task, configuration):#task
    # 建立 Netmiko 连接，使用 telnet 协议和端口号 2000
    conn = task.host.get_connection("netmiko", task.nornir.config)

    # 修改 systemname
    config_commands = ["system-name uian1"]
    result = task.run(task=netmiko_send_config, name="Configure system name", config_commands=config_commands, connection=conn,delay_factor=20)
    print(result)
    # 配置 loopback0 IP 地址
    config_commands = ["interface loopback0", "ip address 10.1.1.1 255.255.255.0"]
    result = task.run(task=netmiko_send_config, name="Configure loopback0", config_commands=config_commands, connection=conn,delay_factor=20)

    # 检查是否开启了 SSH 服务
    command = "display ssh server status"
    result = task.run(task=netmiko_send_command, name="Check SSH service", command_string=command, connection=conn,delay_factor=20)
    output = result.result

    if "SSH server is enabled" in output:
        print(f"SSH service is enabled on {task.host}")
    else:
        print(f"SSH service is not enabled on {task.host}")

# 调用任务函数并传入目标设备信息
result = nr.run(task=configure_router, configuration="router") 
#router是config.yaml中的group，config.yaml里面没有router


if __name__ == "__main__":
    print_result(result)




