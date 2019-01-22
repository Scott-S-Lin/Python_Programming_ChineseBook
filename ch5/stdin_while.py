#filename:stdin_while.py
#function:The stdin.readline() and sys.stdout.write(...)
#We use while loop for keyin the data until Ctrl+D for while loop break

import sys
print("use readline and write")
while True:
   line=sys.stdin.readline()
#sys.stdout.write(line)
   if not line:  #check if EOF or not
       break
   sys.stdout.write('>'+line.upper()) 
print("exit from while")

print("use readline and print")
while True:
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        sys.stderr.write("KB interrupt")
        break 
    if not line:
        sys.stderr.write("EOF")
        break
    print ("line data is",line)
    
print("\nexit from while")

