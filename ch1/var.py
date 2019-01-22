#filename: var_assign.py
#function: variable and assignment using =
a = 5
b = 3.2
c = "Hello"
print(type(a),'\t', type(b),'\t', type(c))
#you can use this way too , the result is the same as the above 
#a, b, c = 5, 3.2, "Hello"
x = y = z = "same"
print(x,y,z)
print("id of x is ",id(x))
print("id of x is ",id(y))
print("id of x is ",id(z))
#del x
#print(x,y,z)

retired_salary=60000
print(type(retired_salary))
retired_salary=retired_salary*(1+0.18)
print(type(retired_salary))


