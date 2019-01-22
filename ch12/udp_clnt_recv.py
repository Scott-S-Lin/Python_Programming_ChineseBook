#filename :udp_clnt_recv.py
#function :sending the data using UDP
# UDP client, creating a socket and send the data thru the socket
import socket
import sys

# create the UDP socket
try:
    UDP_clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except:
    print("\n socket error")
else:
    print("\n socket created\n",UDP_clientSock )

msgdata = "Python is useful for college student, even for Kid's study\n"

ipaddr = ("localhost",1000)

print("\n.... Sending data......")
try:
     UDP_clientSock.sendto(b'msgdata',ipaddr)
except:
    print("\n error send")
else:
    print(" ok send")

#UDP_clientSock.setblocking(1),#UDP_clientSock.settimeout(5)

print("\n .....Receiving the data....")
try:
   reply =UDP_clientSock.recv(1024)
except socket.error:
   print("recv error")
else:
   print("ok",reply)
UDP_clientSock.close()
sys.exit()
