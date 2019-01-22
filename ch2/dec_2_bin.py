#filename:dec_2_bin.py
#function: convert decimal number into binary number

def dec_binary(n):
   if n > 1:
       dec_binary(n//2)
   print(n % 2,end = '')

decimal = int(input("Enter an integer: "))
dec_binary(decimal)
