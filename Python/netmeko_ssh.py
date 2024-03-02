from netmiko import ConnectHandler
from getpass import getpass
password = getpass()
RTR_10 = {
    'ip':   '192.168.126.141',
    'username': 'hocine',
    'password': 'bbb',
    'device_type': 'cisco_ios',
}

net_connect = ConnectHandler(**RTR_10)

config_commands = [ 'int lo0',
                    'ip add 1.1.1.1 255.255.255.0',
                    'no shut' ]
output = net_connect.send_config_set(config_commands)
print(output)

output = net_connect.send_command('show ip int brief')
print(output)