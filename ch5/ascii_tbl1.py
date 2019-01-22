#filename:ascii_tbl1.py
#function: display the asciitable, but clear screen first 
#We use the stdin to read the integer for starting (2 digit)
#use stdin to read the stoping (3 digit)
#and then use the readline() to read the stdin buffer data
"""If there was more than one character to be read at that point (e.g. the newline
that followed the two character that was read in)
We need use next read() or readline() to read characters that are still be in the buffer
It means progarm is waiting for the next read() or readline().
so it is better to use another read() or readline() to read the data in the buffer
"""
"""
and we use the starting and stoping to display the ascii code
we use the starting is 33, stoping is 127 for ascii code print
"""

#clear the screen 
import os
os.system('cls')    # window system use this to celar screen
#os.system('clear') #for Linux
from sys import stdin


starting = stdin.read(2)
stoping = stdin.read(3)
lineinput = stdin.readline()
print ("starting=",starting)
print ("stopping=",stoping)
print ("linedata=",lineinput)

for val in range(int(starting), int(stoping)):
    if (int(starting) - val) % 10 == 0:  # each line contains 10 ascii code
        print("\n")
    print(chr(val), end=' ')
    


