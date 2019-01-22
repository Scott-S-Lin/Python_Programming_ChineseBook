
#filename:Chap_ex_1.py

#create system administrators set
administrator = {'Steven','Bob'}  
users = {'Steve', 'Simon', 'Steven','Louis','Jason'}

print(" Admins  super user")
for user in administrator:
     print(user)

print(" Normal user")     
for user in users:
     print(user)
 
print("please key in the admin user")    
admin_user = input()

for user in administrator:
#    print("user=",user)
    if admin_user == user:  
        print("You are Admin user", admin_user)
        break

diff =administrator.difference(users)
print("difference is in Admin , but not in users set ",diff)

    
print("\nAre admin and user", administrator & users )    
print("\nAre admin or user", administrator | users  )   

print("\nAre Admin but not user",administrator - users )  
print("\nXOR for Admin , user",administrator ^ users  )   

