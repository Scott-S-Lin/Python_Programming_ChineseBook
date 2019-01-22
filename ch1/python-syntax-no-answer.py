#filename:Python-syntax-no-ans.py
#function:To show the Block arrangement
def myrange(n):
    x=0
    while True:
        yield x
        x=x+1
        print("x=",x)
        if x==n:
            break
    print(list(myrange(5)))
