
#filename:operator_ex.py
#function: test the operator or

data1, data2 = "john", None
print( data1 or data2)

var1, var2= 100, ""
print( var1 or var2)

x=10
y=20
print('x != y is',x!=y)

x=0b11111111
y=0b00000000
print(x&y)
z=x|y
print(bin(z))
