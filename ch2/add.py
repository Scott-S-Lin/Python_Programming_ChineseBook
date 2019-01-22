#filename:add.py (in chap2)
#function: adding the total according to two parameter a, and b
#we define adding(paramater1, parameter2)


def adding(a,b):
    total = 0
    in1 = a
    while in1 <= b:  
        total += in1 
        in1 += 1
    return total

print("\n pls keyin the starting and ending data, they are passed to function named adding(para1, para2)")
act1=input()
act2=input()

#call the adding function using adding(parameter1, parameter2)
#please be careful of the int(act1), int(act2) since it will be used for adding the total
#int(act1), int(act2) is uesed to covert teh act1 act2 to integer 

ret_total=adding(int(act1),int(act2))
print("\n ret total from function adding is \t",ret_total)


