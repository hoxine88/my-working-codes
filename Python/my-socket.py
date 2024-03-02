import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("socket successfully created")
except socket.error as err :
    print (f'there error in creating socket with error {err}')
port = 80
try:
    host_ip = socket.gethostbyname("www.github.com")
except socket.gaierror:
    print ("dns error")
    sys.exit()
s.connect((host_ip, port))
print (f'socket successfully to site in {host_ip}')