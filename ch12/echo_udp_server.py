#filename:echo_udp_server.py
#function: nudp server,
#step1: create socket and bin address
#step2: receive and send
#Messages READ  from the socket using recvfrom()
#it returns the data as well as the address of the client

import socket
import sys

# Create a UDP/IP
UDPsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPsock.setblocking(1)
UDPsock.settimeout(5)

# Bind the socket to the port
UDP_server = ('localhost', 10000)
print (sys.stderr, '\nstarting on %s port %s' % UDP_server)

try:
    UDPsock.bind(UDP_server)
except:
    print("\n bind error")
else:
    print("\n binding ok")

while True:
    print (sys.stderr, '\nwaiting to receive message')
    try: 
        data, address = UDPsock.recvfrom(4096)
    except socket.timeout:
        print("\n timeout")
    else:
        print (sys.stderr, 'received %s bytes from %s' % (len(data), address))
        print (sys.stderr, data)
    finally:
        print("\n just check")
    
    if data:
        sentdata = UDPsock.sendto(data, address)
        print (sys.stderr, 'sent %s bytes back to %s' % (sentdata, address))
    else:
        sys.exit(1)
UDP.close()
