#filename:ex5-2.py
#function: the codec encode and decode
#Question : please try to write the Data you key in to the file employee.txt
#and then you can check the file content is 歐巴馬 from using the notepad++

import codecs
import sys

emp_list = list()

keyinagain = input('Press y when you want to keyin more:')
while keyinagain == 'y':
    emp_data = input('Keyin Data: ')
    emp_list.append(emp_data)
    keyinagain = input('Press y if you want to enter more emp_list: ')
    
fileout_emp = open("employee.txt", "w")    
for emp_data in emp_list:
    print("data for write is \t",emp_data)
    codecs.encode(emp_data,'utf-8')
    fileout_emp.write(emp_data)
fileout_emp.close()



