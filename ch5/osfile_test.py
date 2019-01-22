#filename: osfile_test.py
#function: get the file stat using system call stat() and example of filecmp.cmp()
""" import os : is used for OS.remove(filename)
import sys: is used for sys.stdout.write(data)
os.rename(current_file_name, new_file_name)
os.rename("employeeB.txt", "employeeBB.txt")
"""

import os
import sys

with open("ascii_tbl1.py", "r") as file_in:
  with open("employeeB.txt", "w") as file_out:
      for line in file_in:
#        sys.stdout.write(line)
        file_out.write(line)

#this section program will print the content of ascii_tbl1.py 
print("\n\nThe following is the data file after copy\n")
with open("employeeB.txt", "r") as file_in:
    for line in file_in:
         sys.stdout.write(line)


import filecmp
print ('--->compare the files it is true if they are the same:' )
print (filecmp.cmp('employeeB.txt','ascii_tbl1.py'))

from shutil import *
import time
stat_info=[]

def file_info(file_name):
    global stat_info
    stat_info = os.stat(file_name)
    print( '\tMode     :', stat_info.st_mode)       
    print( '\tinode no :', stat_info.st_ino)        #Inode number
    print( '\tuser id  :', stat_info.st_uid)        #user id
    print( '\tgroup id :', stat_info.st_gid)        #group id
    print( '\tFile size:', stat_info.st_size)       #file size
    print( '\tdevice   :', stat_info.st_dev)        #device
    print( '\tno of hardlink:', stat_info.st_nlink) #no of hard link
    print( '\tCreated  :', time.ctime(stat_info.st_ctime))
    print( '\tAccessed :', time.ctime(stat_info.st_atime))
    print( '\tModified :', time.ctime(stat_info.st_mtime))

file_info('employeeB.txt')

print("\nThe file stat is\n ",stat_info)

os.rename("employeeB.txt", "employeeBB.txt")
os.remove("employeeBB.txt")
#os.mkdir('example')
#print ('SOURCE:')

