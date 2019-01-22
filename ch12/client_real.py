#filename:client_real.py
#function: client using
#step1: create socket
#step2: connect to server

import socket # for socket
import sys
PORT=80       #default port for socket

#step1: create socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print( "Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print ("there was an error resolving the host")
    sys.exit()

#step2: connect to the server
s.connect((host_ip,PORT))

print ("socket connected to google IP == %s" %(host_ip))
# receive data from the server
try:
#   recv_msg=s.recv(1024)
    recv_msg=s.write("test")
except:
    print("\n receiving error")
else:
    print(recv_msg)
s.close() 
