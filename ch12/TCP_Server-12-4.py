#filename:TCP_Server-12-4
#function: Server socket using TCP
#step1. create socket and bind
#step2. listen and accept
#step3: and then recv and send the message

import socket
import sys
 
HOST = ''   # all available interfaces
PORT = 8888 # non-privileged port

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


#Step2: listen, set the queue , how many app can work 
s.listen(10)
print ('Socket is listening')

# Step3: wait to accept a connection - from client connect()blocking call
try:
    print("try to accept the connect!!!!")
    conn, addr = s.accept()
except :
    print("error connection")
else: 
    print ( 'Connected from ' + addr[0] + ':' + str(addr[1]))

#step4:recv and sendall with client
try:
    recv_message = conn.recv(1024)
#    recv_message = s.recv(1024)
except socket.timeout:
    print("timeout")
else:
    print("receive ok")

reply_message = 'ACK to you from server...' + recv_message
if not recv_message: 
     print("no receive data")
     
print("sendall") 
conn.sendall(reply_message)
conn.close()
s.close()
sys.exit()




