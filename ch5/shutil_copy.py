#filename: shutil_copy.py
#function: mkdir using OS method os.mkdir(….)
#need import sys for sys.stdout.write(...)
"""1.os.getcwd(): this method displays the current working directory.
Return a string representing the current working directory.
1. Dirctory: is a file whose data is a sequence of entries, each consists of
   a in inode number and the name of a file contained in the directory
2. Directory layout consists of Inode no and filenames
3. os.getcwd() method displays the current working directory.
"""

import sys
from shutil import *
import os

currentdir=os.getcwd()
sys.stdout.write(currentdir)


if not os.path.exists('testdir'):
    os.mkdir('testdir')

#print ('\nlist of testdir before copy:', os.listdir('testdir'))
#copy('shutil_copy.py', 'testdir')
#print( 'list of testdir after copy:', os.listdir('testdir'))
#for file in os.listdir('testdir'):
#   print ("\nfile in directory\n",file)
   
dirlist=os.listdir(os.getcwd())
print("\nfile list before sort\n",dirlist)
dirlist.sort()
print("\nfile list after sort\n",dirlist)

dirname = "c:\\"
print("\n Root directory:\n",os.listdir(dirname))


import os, time, shutil, sys

work_path = 'd:\\Backup-CF-card\\'
#check if the directory is empty
try:
    if os.listdir(work_path)=="":
        print ("yes it is empty",os.listdir(dirname))
    else:
        print (work_path,"Not empty directory ")
except FileNotFoundError:
    sys.exit()  
