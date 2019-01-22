#filename:return-none.py
#function: return None, or only return, or no return
#you can see the result is return None after you call the following three functions
def noreturn():
    print("function noreturn")

def return_none():
    print("function return_none")
    return None
def returnnothing():
    print ("function returnnothing")
    return

print("the return after calling noreturn is-->",noreturn())
print("the return after calling return_none is-->",return_none())
print("the return after calling returnnothing is-->",returnnothing())
