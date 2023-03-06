from netmiko import platforms
 
for i in platforms:
    print(i)
 
ssh_platforms = [i for i in platforms if 'telnet' not in i and 'serial' not in i and 'ssh' not in i]
ssh_platforms.remove('abc')
ssh_platforms.remove('autodetect')
ssh_platforms.remove('terminal_server')
 
telnet_platforms = [i for i in platforms if 'telnet' in i]
serial_platforms = [i for i in platforms if 'serial' in i]
 
print(ssh_platforms)
print(len(ssh_platforms))
print(telnet_platforms)
print(len(telnet_platforms))
print(serial_platforms)
 
