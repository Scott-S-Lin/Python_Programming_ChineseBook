#python sys_path.py
#function :import something
#format: import modulename1, modulename2,......
#dir() is used to list names a module_names.
#dir() will return a sorted list of module name,  dir() not list the names of built-in functions and variables.
#dir(object) is built-in function, if the object is module name, it will return the names of module
#dir(__builtins__),If you want those, they are defined in the module __builtins__


import sys
print("\n Path serach :\n")
for searchpath in sys.path:
 print (searchpath," ")

print("\n Append system path:\n")
newpath='d:/c++/'
sys.path.append(newpath)
for searchpath in sys.path:
 print (searchpath," ")
 
print("\n***dir****\n",dir())
print("\n***dir sys ****\n",dir(sys))

#print("\n****Builtin****\n",dir(__builtins__))

