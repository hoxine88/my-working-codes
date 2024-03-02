from netmiko import ConnectHandler
from operator import itemgetter

RTR_10 = {
    'ip':   '192.168.126.141',
    'username': 'hocine',
    'password': 'bbb',
    'device_type': 'cisco_ios',
}
print ('Checking interface status..')
net_connect = ConnectHandler(**RTR_10)

output = net_connect.send_command('show ip int brie', use_textfsm=True)



devlist = []
for i in output:
    if i['status'] == 'up':
        devlist.append(i['interface'])
print(devlist)

print([i for i in output if i['status'] == 'up'])
print ([i['interface'] for i in output if i['status'] == 'up'])

print('\n \n')

print ('\nList of interfaces which are UP \n')
statusup =[i['interface'] for i in output if i['status'] == 'up']

for ifaceup in statusup:
    print (ifaceup)

print ('\nList of interfaces which are DOWN \n')
statusother =[i['interface'] for i in output if i['status'] != 'up']
for ifaceother in statusother:
    print (ifaceother)
