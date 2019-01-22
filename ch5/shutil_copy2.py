#filename: shutil_copy2.py
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
   
dirlist=os.listdir(os.getcwd())
#print("\nfile list \n",dirlist)
dirlist.sort()
#print("\nfile list after sort\n",dirlist)

work_path = 'd:\\book\\chap1\\'
#check if the directory is empty
try:
    if os.listdir(work_path)=="":
        print ("\nyes it is empty",os.listdir(dirname))
    else:
        print (work_path,"\nNot empty directory ")
except FileNotFoundError:
    sys.exit()  
