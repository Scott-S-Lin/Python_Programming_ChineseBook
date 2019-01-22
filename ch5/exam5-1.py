#filename:ex5-1.py(it is listdir.py)
#function :listdir and count how many files with filename.txt

from shutil import *
import os
import os.path

current_dir=os.getcwd()
print("current directory is",current_dir)

file_txt_total=0
file_total=0
print(os.listdir(current_dir))

for fname in os.listdir('.'):
    if os.path.isfile(fname):
       file_total +=1
       if fname[-4:]=='.txt':
           print("filename is ", fname)
           file_txt_total +=1
 

print("total file no=",file_total)
print("total txt file no=",file_txt_total)

