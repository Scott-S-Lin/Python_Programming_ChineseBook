#filename:TCP-socket-12-3.py
#function:Client to create an TCP IP using AF_INET, SOCK_STREAM socket
#AF_INET is Internet Protocol,#SOCK_STREAM is TCP
#connect to server: s.connect((ip , port))
#send using    socketname.sendall(b'message')
#receive using replydata = socketname.recv(4096)


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


host ="www.python.com"
port = 80
BUFSIZE=1024 
#HOST = 'daring.cwi.nl'    # The remote host
#PORT = 50007              # The same port as used by the server

 
try:
    ip = socket.gethostbyname( host )
#    ip = socket.gethostbyname( HOST )
except socket.gaierror:
    #could not resolve
    print ('Hostname not found. abnormal exit')
    sys.exit()  
print ('Ip of '+host + ' is : ' + ip)
 
#Connect to server
s.connect((ip , port))
print (TCPorUDP[TCP_or_UDP]+' Socket Connected to ' + host + ', ip addres is ' + ip)

message = "GET / HTTP/1.1\r\nHost: oschina.net\r\n\r\n"
 
try :
    #Set the whole string
    s.sendall(b'message')
except socket.error:
    print ('Send failed')
    sys.exit()
else: 
    print ('\nMessage send successfully')
 

print("\n .....Receiving the data....")
try:
   reply = s.recv(4096)
except socket.error:
   print("recv error")
else:
   print("ok")
   
if not reply:
    print("reciving is NG")
else:   
    print ("\nThe receving data=\n",reply)
s.close()
sys.exit()





