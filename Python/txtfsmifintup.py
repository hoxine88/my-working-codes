from netmiko import ConnectHandler
#from operator import itemgetter
from getpass import getpass
password = getpass()
RTR_10 = {
    'ip':   '192.168.126.141',
    'username': 'hocine',
    'password': 'bbb',
    'device_type': 'cisco_ios',
}
print ('Checking interface status..')
net_connect = ConnectHandler(**RTR_10)

output = net_connect.send_command('show ip int brie', use_textfsm=True)

#Fetch data from dict and print
name = output[2]['interface']
status = output[2]['status']
print ('\nInterface ' + name + ' status is ' + status )

if status == 'up':
    print ('Finishing the script')
else :
    print ('making backup interface UP')
    config_commands = [ 'int loopback40',
                        'no shut' ]
    output = net_connect.send_config_set(config_commands)
    print (output)
    print ('Finished configuration')
