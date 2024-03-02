from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException
from netmiko.exceptions import NetmikoAuthenticationException
### you can use 2 file and inside them you can insert the differnet ip address
### for ex file1 has ip 192.168.126.141 and file2 has 192.168.126.141 and you use IP list = open (file1)
RTR_10 = {
    'ip':   '192.168.126.141',
    'username': 'hocine',
    'password': 'bbb',
    'device_type': 'cisco_ios',
}
print ('connecting to device ' + str(RTR_10['ip']) +'#######')
try :

    net_connect = ConnectHandler(**RTR_10)
except NetmikoTimeoutException :
    print ('the device in not reachable')
except NetmikoAuthenticationException :
    print ('the credential in not correct')
except SSHException:
    print ('Make sure SSH is enabled in device.')
output = net_connect.send_config_from_file(config_file = '16_config.txt')
print(output)

print ('\n saving the config\n')
output = net_connect.save_config()
print(output)

output = net_connect.send_command('show ip int brief')
print(output)

RTR_11 = {
    'ip':   '192.168.126.142',
    'username': 'hocine',
    'password': 'bbb',
    'device_type': 'cisco_ios',
}
print ('connecting to device ' + str(RTR_11['ip']) +'#######')
try :

    net_connect = ConnectHandler(**RTR_11)
except NetmikoTimeoutException :
    print ('the device in not reachable')
except NetmikoAuthenticationException :
    print ('the credential in not correct')
except SSHException:
    print ('Make sure SSH is enabled in device.')
output = net_connect.send_config_from_file(config_file = '15_config.txt')
print(output)

print ('\n saving the config\n')
output = net_connect.save_config()
print(output)

output = net_connect.send_command('show ip int brief')
print(output)