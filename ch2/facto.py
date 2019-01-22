#filename:facto.py
#function: fcatorial function using the recursive way

#n! = n * (n-1)!, if n = 1 and f(1) = 1
#3! = 3 * 2!
#2! = 2 * 1

def factorial(n):
    print("factorial called  n = ",n)
    if n == 1:
        return 1
    else:
        print("n,factorial(n-1) n=",n)
        return n * factorial(n-1)

print("\npls input the n for n! function call")
arg=int(input())
print("final n! =",factorial(arg))
