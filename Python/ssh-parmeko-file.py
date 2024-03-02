import paramiko
import time
from getpass import getpass #this line is optional 


username = 'hocine'
password = 'bbb'

with open('file.txt') as DEVICE_LIST:
	for RTR in DEVICE_LIST:
		try:
			print ('\n #### Connecting to the device ' + RTR + '####\n' )
			SESSION = paramiko.SSHClient()
			SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			SESSION.connect(RTR.strip(), port=22,
							username=username,
							password=password,
							look_for_keys=False,
							allow_agent=False)

			DEVICE_ACCESS = SESSION.invoke_shell()
			DEVICE_ACCESS.send(b'config t\n')
			for N in range (2,5):
				DEVICE_ACCESS.send('int lo ' +str(N) + '\n')
				DEVICE_ACCESS.send('ip address 1.1.1.' +str(N) + ' 255.255.255.255\n')  

			time.sleep(3)
			DEVICE_ACCESS.send(b'do term length 0\n')
			DEVICE_ACCESS.send(b'do show ip int brief\n')
			time.sleep(3)
			output = DEVICE_ACCESS.recv(65000)
			print (output.decode('ascii'))

			SESSION.close()
		except Exception as e:
			print(f"Error connecting to {RTR.strip()}: {e}")