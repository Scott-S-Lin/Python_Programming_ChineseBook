#filename:ex2-1.py
#funcion: check the local and global var 

x = 102
def local_func():
   x = 108
   print (x)
 
local_func()
print(x)
