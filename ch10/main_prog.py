#filename:main_prog.py
#funcion : main program for integration project
#format: import Modulename1,Modulename2,......
#usage : modulename.function
#        modulename.variable

import fibo
para=int(input("please keyin the top number for fibo:"))
result=fibo.fib(para)
print("\nfibo value after use the module function=",result)


a=int(input("\nplease input the GCD parameter a: "))
b=int(input("please input the GCD parameter b: "))
result=fibo.gcd(a,b)
print("\nGCD value after use the module function=",result)

