from netmiko import ConnectHandler
IP_LIST = open('15_devices.txt')
for IP in IP_LIST:
    print ('\n ##### '+ IP.strip() + ' ##### \n' )
    RTR = {
    'ip':   IP,
    'username': 'hocine',
    'password': 'bbb',
    'device_type': 'cisco_ios',
    }

    net_connect = ConnectHandler(**RTR)

    output = net_connect.send_config_from_file(config_file = '15_config.txt')
    print(output)

    output = net_connect.send_command('show ip int brief')
    print(output)