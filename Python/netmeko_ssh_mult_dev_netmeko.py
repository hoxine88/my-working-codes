from netmiko import ConnectHandler

RTR_1 = {
    'ip':   '192.168.126.141',
    'username': 'hocine',
    'password': 'bbb',
    'device_type': 'cisco_ios',
	}

RTR_2 = {
    'ip':   '192.168.126.142',
    'username': 'hocine',
    'password': 'bbb',
    'device_type': 'cisco_ios',
	}
RTR_3 = {
    'ip':   '192.168.126.143',
    'username': 'hocine',
    'password': 'bbb',
    'device_type': 'cisco_ios',
	}
	

DEVICE_LIST = [RTR_1, RTR_2, RTR_3]
for DEVICE in DEVICE_LIST:
    print ('Connecting to the Device ' + DEVICE['ip'])
    net_connect = ConnectHandler(**DEVICE)

    config_commands = [ 'int lo0',
                        'ip add 1.1.1.1 255.255.255.0',
                        'no shut' ]
    output = net_connect.send_config_set(config_commands)
    print(output)

    output = net_connect.send_command('show ip int brief')
    print(output)