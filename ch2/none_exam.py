#function:Nono is used when we encounter the following cases
'''
1.Void functions that do not return anything will return a None object.
2.None is returned by functions in which the program does not encounter a return statement
'''

def none_return_function(var_a):
    if (var_a % 2) == 0:
        return True

def void_function(): 
    data1 = 100
    data2 = 2000
    sum = data1 + data2
    
return_value = none_return_function(5)
print(return_value)

return_value = none_return_function(4)
print(return_value)
    
print("Function no return value example , the return will be ",end=" ")
return_value = void_function()
print(return_value)
