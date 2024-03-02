from netmiko import ConnectHandler
with open('15_devices.txt') as IP_LIST:
	for IP in IP_LIST:
		IP = IP.strip()
		RTR = {
		'ip':   IP,
		'username': 'hocine',
		'password': 'bbb',
		'device_type': 'cisco_ios',
		}
		
		net_connect = ConnectHandler(**RTR)
		config_commands = [ 'int lo0',
                            'ip add 1.1.1.1 255.255.255.0',
                            'no shut' ]
		output = net_connect.send_config_set(config_commands)
		print(output)
		output = net_connect.send_command('show ip int brief')
		print(output)
		