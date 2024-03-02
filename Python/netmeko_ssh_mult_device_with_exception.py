from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException
from netmiko.exceptions import NetmikoAuthenticationException
IP_LIST = open('15_devices.txt')
for IP in IP_LIST:
    print ('\n ##### '+ IP.strip() + ' ##### \n' )
    RTR = {
    'ip':   IP,
    'username': 'hocine',
    'password': 'bbb',
    'device_type': 'cisco_ios',
    }
    print ('connecting to device ' + IP +'#######')
    try :

        net_connect = ConnectHandler(**RTR)
    except NetmikoTimeoutException :
        print ('the device in not reachable')
        continue      #### this very important other wise it will not continue it is used for for loop to continue
    except NetmikoAuthenticationException :
        print ('the credential in not correct')
        continue
    except SSHException:
        print ('Make sure SSH is enabled in device.')
        continue

    output = net_connect.send_config_from_file(config_file = '15_config.txt')
    print(output)
    
    print ('\n saving the config\n')
    output = net_connect.save_config()
    print(output)

    output = net_connect.send_command('show ip int brief')
    print(output)