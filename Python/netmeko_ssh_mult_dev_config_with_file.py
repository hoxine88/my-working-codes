
from netmiko import ConnectHandler
with open('15_devices.txt') as IP_LIST:
    for IP in IP_LIST:
        RTR = {
        'ip':   IP,
        'username': 'hocine',
        'password': 'bbb',
        'device_type': 'cisco_ios',
		'global_delay_factor': 2,
        }

        net_connect = ConnectHandler(**RTR)

        with open('15_config.txt') as CONFIG_LINES:
            CONFIG = CONFIG_LINES.read()
        output = net_connect.send_config_set(CONFIG)
        print(output)

        output = net_connect.send_command('show ip int brief')
        print(output)

        

