#filename: osfile.py
#function: remove file and rename file
""" import os : is used for OS.remove(filename)
import sys: is used for sys.stdout.write(data)
os.rename(current_file_name, new_file_name)
os.rename("employeeB.txt", "employeeBB.txt")
"""

import os
import sys

with open("employee1.txt", "rt") as file_in:
  with open("employeeB.txt", "wt") as file_out:
      for line in file_in:
        sys.stdout.write(line)
        file_out.write(line)

print("\n\nThe following is the BACKUP data file before REMOVE\n")
with open("employeeB.txt", "rt") as file_in:
    for line in file_in:
        sys.stdout.write(line)
        
os.rename("employeeB.txt", "employeeBB.txt")
os.remove("employeeBB.txt")
