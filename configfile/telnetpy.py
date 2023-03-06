# from nornir import InitNornir
# from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
# from nornir.core.filter import F

# nr = InitNornir(config_file="config.yaml")

# def telnet_task(task, loginname):
#     # 定义提示符
#     prompt = f"{task.host}>"
#     # 使用 netmiko 的 send_command 方法进行 telnet 登录，并输入用户名和密码
#     output = task.run(task=netmiko_send_command, 
#                       command_string=f"{loginname}\n", 
#                       expect_string="Password:",
#                       strip_command=False,
#                       strip_prompt=False)
#     # 输入密码
#     output = task.run(task=netmiko_send_command,
#                       command_string=task.host.get_password() + "\n",
#                       expect_string=prompt,
#                       strip_command=False,
#                       strip_prompt=False)
#     # 执行一些命令
#     output = task.run(task=netmiko_send_command, 
#                       command_string="show version",
#                       expect_string=prompt,
#                       strip_command=False,
#                       strip_prompt=False)
#     # 返回结果
#     return output.result

# # 运行任务
# result = nr.run(task=telnet_task, loginname="myloginname")
# from nornir import InitNornir
# from nornir.plugins.connections import ConnectionPluginRegister
# from nornir.plugins.tasks.text import SendCommand

# # 注册连接插件
# ConnectionPluginRegister.register("telnet", "nornir.plugins.connections.telnet.Telnet")

# nr = InitNornir(
#     inventory={
#         "plugin": "nornir.plugins.inventory.simple.SimpleInventory",
#         "options": {
#             "host_file": "inventory/hosts.yaml",
#             "group_file": "inventory/groups.yaml",
#             "defaults_file": "inventory/defaults.yaml",
#         },
#     },
#     logging={"enabled": False},
# )

# # 执行 show interface 命令
# result = nr.run(task=SendCommand, command_string="show interface", prompt="R1#")
# from nornir import InitNornir
# from nornir_napalm.plugins.tasks import napalm_cli

# nr = InitNornir(config_file="config.yaml")

# def run_command(task):
#     command = "show interface"
#     result = task.run(task=napalm_cli, commands=[command], transport="telnet")
#     print_result(result)

# def print_result(result):
#     for device_name, multi_result in result.items():
#         print(f"Results for {device_name}")
#         for command_result in multi_result:
#             print(f"Command: {command_result.command}")
#             print(f"Result: {command_result.result}")

# if __name__ == "__main__":
#     result = nr.run(task=run_command)
#     print_result(result)

from nornir import InitNornir
from nornir.plugins.tasks import remote_command

nr = InitNornir(config_file="config.yaml")

def show_interface(task):
    command = "show interface"
    result = task.run(task=remote_command, command_string=command)
    task.host["interface_output"] = result.result

results = nr.run(task=show_interface)
for host, result in results.items():
    print(f"Host: {host}\n{result['interface_output']}")
