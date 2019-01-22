#filename:TCP_Server-12-step1.py
#function: Server socket using TCP
#1. create socket
#2. bind the address

#Step1: create socket and bind the address
import socket
import sys
 
HOST = ''   # all available interfaces
PORT = 8888 # non-privileged port

#PORT =80

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print("Create socket FAIL!!!!")
else:
    print ('Socket created')

s.setblocking(1)
s.settimeout(5)

try:
   s.bind(("127.0.0.1", 0))

except socket.error as msg:
    print('Binding NG.  Code : ' + str(msg[0]) + ' Message: ' + msg[1])
    sys.exit()
     
print ("Binding the address OK!")
