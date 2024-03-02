from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException
from netmiko.exceptions import NetmikoAuthenticationException
import time
import datetime
TNOW = datetime.datetime.now().replace(microsecond=0)
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
    
    print ('\n saving the config\n')
    output = net_connect.send_command('show run')
    print(output)
    
    SAVE_FILE = open("RTR_"+IP +'_'+ str(TNOW), 'w')
    SAVE_FILE.write(output)
    SAVE_FILE.close
    print ('Finished config backup')