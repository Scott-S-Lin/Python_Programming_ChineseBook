#filename:read_write.py
#function:Data write to file and then read data from file
#         by keyinging data each time until your choice is not 'y' 
#we use the list when you keyin the data
#via emp_list  = []  or emp_list = list() for  empty list
#The append method adds a single item to the end of the list by #emp_list_obj.append(item)
 
emp_list = list()

keyinagain = input('Press y when you want to keyin more:')
while keyinagain == 'y':
    emp_data = input('Keyin Data: ')
    emp_list.append(emp_data)
    keyinagain = input('Press y if you want to enter more emp_list: ')

print('Your keyined emp_list data are as follows:')
for emp_data in emp_list:
    print("The data you input is\t",emp_data)
    
# Open a file for writing only
fileout_emp = open("employee.txt", "w")
for emp_data in emp_list:
    print("data for write is \t",emp_data)
    fileout_emp.write(emp_data)
fileout_emp.close()

#Opens a file for reading only
filein_emp = open("employee.txt", "r")
while True:
  emp_data=filein_emp.read()
  if not emp_data: break
  print("\nData from employee.txt file are:", emp_data)
  
#  emp_data=filein_emp.readline()
#  import sys
#  sys.stdout.writelines(emp_data)
  
file_position = filein_emp.tell();
print ("\nCurrent file position : ", file_position)

#filein_emp.seek(0,0);
while 1:
  emp_data=filein_emp.read(5)
  if not emp_data: break
  print("\n Data are using read(count)", emp_data)
  

filein_emp.close()
