#filename:file_obj_attr.py
#function file object atribute

fileo = open("employee.txt", "r")
print ("Name of the file: ", fileo.name)
print ("file Closed? : ", fileo.closed)
if fileo.mode =='r': 
   print ("Opening mode is %s "%fileo.mode,"you have no right to Write")
   import sys
   sys.exit
elif  fileo.mode =='w':
   print(" we will  code something to do some task later")
   pass
