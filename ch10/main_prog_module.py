#filename:main_prog_module.py
#funcion : main program for integration project
#format: import Modulename1,Modulename2,......
#usage : modulename.function
#        modulename.variable
#import fibo 

import fibo
para=int(input("please keyin the top number for fibo:"))
result=fibo.fib(para)
print("\nfibo value after use the module function=",result)


a=int(input("\nplease input the GCD parameter a: "))
b=int(input("please input the GCD parameter b: "))
result=fibo.gcd(a,b)
print("\nGCD value after use the module function=",result)

#The built-in function dir() is used to find out which names a module defines
print("\n\nwhich Names a module of Fibo defines are:\n ",dir(fibo))

#import sys
#print("\nsys",dir(sys))

