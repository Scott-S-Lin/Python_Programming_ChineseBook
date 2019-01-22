#filename:file_fstat.py
#function:
"""file.fileno()is used to return 
the integer file descriptor, used to request I/O operations from the operating system.
"""
#file_obj.fileno() will return the file descriptor
#1.The OS in Linux system has File descriptor table identifies all open files for a process
#The Unix kernel returns a file descriptor for Open and creat system calls, which is an index into the
#    user file descriptor table
#2.When executing read and wtite system calls(we call Method here), the Unix kernel uses the file descriptor
#    to access the user file descriptor table, follows pointers to the file table and inode table entries, and
#3.From the inode, find the data in the file
"""Inodes exist in a static form on disk, disk inodes consists of the following fields in unix: 
1. file owner id: user id, froup id...
2. file type
3. file access permission
4. file access time
5. number of links to the file
6. Table of contents for the disk addresses of data in a file
7. File size.
"""

import sys

fileout = open("log.txt", "w")
filefd= fileout.fileno()
print("file descriptor=",filefd)

print("\n please keyin data until you press Ctrl+D at the same time")
while True:
    data = sys.stdin.readline()
    if not data:
        break
    fileout.write(data)
    fileout.flush()

print("while loop end because you keyin Ctrl+D\n")

print("\nIt show the file stat using os.fstat(file_decriptor)\n")
#need import os, if we want to get the fstat
import os 
print(os.fstat(filefd))

