#filename:adding.py
#function: add the data by starting and ending data

def adding_func(para1=0,para2=50):
    
    total = 0
    i = para1
    while i <= para2:
        print(i," ",para2)
        total += i
        i += 1
    return total

#the function call using the arguments data such as argument1,argument2

print("please keyin data from KB for Starting no and ending no")
arg1=int(input())
arg2=int(input())
total=adding_func(arg1, arg2)
print(total)
