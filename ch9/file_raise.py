#filename:file_raise.py
#function: file read write and raise

import sys

filename=input("pls keyin filename for write:")
try:
   fh = open(filename, "w")
   fh.write("Python raise example\n")
   fh.write("Python is good\n")
   str=input("pls keyin data:")
   fh.write(str) 
except IOError:
   print ("IOError: file not found or read data")
except EOFError:
   print ("EOF error")   
else:
   print ("Data writen ok")
   fh.close()
finally:
   print("finally")

print("\n****Open and read file***")
try:
    filein=input("pls keyin filename for read:")
    with open(filein, "r") as file_in:
        print("file data is as follows")
        print("---------------------")
        for line in file_in:
            sys.stdout.write(line)
        print("\n---------------------")     
except FileNotFoundError:
    print("exception error: file not found")

else:
    print("\nlast line data=",line)
#    raise
#'''
#Traceback (most recent call last):
#  File "D:/Book/Chap9/file_raise.py", line 34, in <module>
#    raise
#RuntimeError: No active exception to reraise
#'''

finally:
    print("finally")
