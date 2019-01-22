#filename :udp_clnt.py
#function :sending the data using UDP
# UDP client, creating a socket and send the data thru the socket

import socket

# create the UDP socket
try:
    UDP_clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except:
    print("\n socket error")
else:
    print("\n socket created\n",UDP_clientSock )

#give the msgdata
msgdata = "Python is useful for college student, even for Kid's study\n"

# setting address using the pair(host, port) format
#ipaddr = ("localhost",21567)
ipaddr = ("localhost",80)

# Sending the data 
print("\n.... Sending data......")
try:
     UDP_clientSock.sendto(b'msgdata',ipaddr)
except:
    print("\n error send")
else:
    print("\n ok send")

