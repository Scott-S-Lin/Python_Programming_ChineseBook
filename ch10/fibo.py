#filename:fibo.py
#function:Fibo module will be used by using import modulename in Python
#return Fibonacci series based on the Top value n

def fib(n): 
    fibresult = []
    a, b = 0, 1
    while b < n:
        fibresult.append(b)
        a, b = b, a+b
    return fibresult

def gcd(m,n):
    while n:
        m,n = n,m%n
    return m
