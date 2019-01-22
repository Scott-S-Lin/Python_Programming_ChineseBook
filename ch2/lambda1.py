#filename:lamda1.py
#function:Anonymous functions
#limitation:Lambda functions are restricted to a single expression
#used:can be used wherever normal functions can be used.

min = lambda a, b: a if a < b else b
max = lambda a, b: b if a < b else a
max = lambda a, b: b if a < b else a
str = lambda a, b: a+b
sub = lambda a, b: a-b
z = lambda x: x * y

print(min(100, 98)) 
print(max(96, 99))
print(max("abc","Abc"))
print(str("abc","Abc")) 
print(sub(100, 98))

print("pls key in your retired salary")
y=int(input())
print("you can get total money from salary and interest",z(1.18))
