#filename:list_access.py

import string

Password_string = "She101Who"
print(Password_string)
isnumbers = [x for x in Password_string if x.isdigit()]
print( isnumbers)
print(len(isnumbers))

    
Password_new=[]
for x in Password_string:
   Password_new.append(chr(ord(x)+3))
print("password new=",Password_new)

index=0
for item in Password_new:
 print(item,end=' ')
 if Password_new[index].isdigit():
    Password_new[index]=chr((ord(Password_new[index])+3))
 index+=1
print("\n",Password_new)

#change from List to string
finalstr=''.join(Password_new)
print("\n",finalstr)



