import paramiko
import time
from getpass import getpass #this line is optional 
#please be really care about RTP.strip alwys do it like that otherwise it will not work


username = 'hocine'
password = 'bbb'

with open('file.txt') as DEVICE_LIST:
	for RTR in DEVICE_LIST:
		try:
			print ('\n #### Connecting to the device ' + RTR.strip() + '####\n' )
			SESSION = paramiko.SSHClient()
			SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			SESSION.connect(RTR.strip(), port=22,
							username=username,
							password=password,
							look_for_keys=False,
							allow_agent=False)
			DEVICE_ACCESS = SESSION.invoke_shell()
			DEVICE_ACCESS.send(b'terminal len 0\n')
			DEVICE_ACCESS.send(b'show run\n')
			time.sleep(6)
			output = DEVICE_ACCESS.recv(65000)
			print (output.decode('ascii'))
			SAVE_FILE=open ('ROUTER' + RTR.strip() + 'config' , 'w')
			SAVE_FILE.write(output.decode('ascii'))
			SAVE_FILE.close
			
			SESSION.close()
		except Exception as e:
			print(f"Error connecting to {RTR.strip()}: {e}")
