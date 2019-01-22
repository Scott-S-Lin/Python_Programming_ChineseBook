#filename:while-loop.py
#function while loop (in chap1)

import sys

message_text = 'coap protocol for some IoT projects'
count = 0
max=len(message_text)

sys.stdout.write('The char is:')
while (count < max):
#   print ('The char is:', message_text[count])
   sys.stdout.write(message_text[count])
   count = count + 1

#   print("you are good for while loop")
   
print ("\nvvvvv Good boy vvvvv!")
