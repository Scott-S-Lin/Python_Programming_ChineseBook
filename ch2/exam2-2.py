#filename:ex2-2.py
#funcion: check the local and global var 

x = 102
def local_func():
   global x
   x = 108
   print (x)
 
local_func()
print(x)
