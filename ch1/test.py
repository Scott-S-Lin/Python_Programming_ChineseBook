#filename:test.py
#function: first program for Python 3.4.3
#file location :c:\book\chap1

account_name="John Wang"
account_no="00810381686888"
openaccount_money = 100;

if ( openaccount_money  == 100 ) :
    print("Value of money for open account is 100 NTD")

print("\n please keyin the money ")
money=input()
print("Value of money you deposit is ",money)

openaccount_money =openaccount_money+ int(money)
print("total money now in your acoount",account_no, " is",openaccount_money)
print ("Have a nice day!", account_name)

#the following is for your reference only, you can see after we discuss string covert to int int(string)
#Traceback (most recent call last):
#  File "C:\Python34\test.py", line 13, in <module>
#    openaccount_money =openaccount_money+ money
#TypeError: unsupported operand type(s) for +: 'int' and 'str'


#program output:
#Value of money for open account is 100 NTD

# please keyin the money 
#200
#Value of money deposit is  200
#total money now in your acoount 00810381686888  is 300
#Have a nice day! John Wang
