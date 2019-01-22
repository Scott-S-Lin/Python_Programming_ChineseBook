#filename:TCP-socket-12-1.py
#function:create an TCP IP using AF_INET, SOCK_STREAM socket
#AF_INET is Internet Protocol
#SOCK_STREAM is TCP
import socket   #for sockets
import sys      #for exit
 
try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print (' socket created faile and Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit();
else:
    print("Socket Created sucessfully")
finally:
    print("exit")

