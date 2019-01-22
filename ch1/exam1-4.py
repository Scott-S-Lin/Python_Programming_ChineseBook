#filename:ex1-4.py
#function:bitwise operation

x=0b10101010
y=0b01010101
print("x y= %x %x"%(x,y))
print("after bit operator AND, data is ",x&y)
z=x|y
print("after OR operator data is",bin(z))
print("after OR operator data is %d using decimal format"%z)
