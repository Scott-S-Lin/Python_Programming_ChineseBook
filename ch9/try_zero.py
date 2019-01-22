#filename: try_zero.py in chap9
#function: the try ZerodividionError exception

def divide(x, y):
     try:
         result = x / y
     except ZeroDivisionError:
         print ("division by zero , it is exception error")
     except Nameerror:
         print("Name error")
     else:
         print ("result=%2.1f" %result)
     finally:
         print ( "executing finally ")
         
 

try:
     x=int(input("keyin x for the dividend:"))
     y=int(input("keyin y for divisor:"))
except ValueError:
     print (' Must keyin a numeric value!')
else:
    print("right input")

#call subprogram divide function
z=divide(x,y)
