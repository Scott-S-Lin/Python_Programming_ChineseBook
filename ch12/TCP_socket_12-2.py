#filename:TCP-socket-12-2.py
#function:create an TCP IP using AF_INET, SOCK_STREAM socket
#AF_INET is Internet Protocol
#SOCK_STREAM is TCP
#connect to server: s.connect((ip , port))

import socket   #for sockets
import sys      #for exit

#Step1: create the socket
TCP_or_UDP=1
TCPorUDP=["UDP","TCP"]

try:
   if TCP_or_UDP==True:
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   else:
       s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       print("Using UDP")
except socket.error as msg:
    print (' socket created faile and Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit();
else:
    print(TCPorUDP[TCP_or_UDP]+" Socket Created sucessfully")
finally:
    print("Finally")

#Step2: connect to the remote Server

#host = 'www.oschina.net'
host ="www.python.com"
port = 80
 
try:
    ip = socket.gethostbyname( host )
except socket.gaierror:
    #could not resolve
    print ('Hostname not found. abnormal exit')
    sys.exit()  
print ('Ip of '+host + ' is : ' + ip)
 
#Connect to server
s.connect((ip , port))
print (TCPorUDP[TCP_or_UDP]+' Socket Connected to ' + host + ', ip addres is ' + ip)
