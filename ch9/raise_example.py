#filename:raise_exmple.py
#function : raise by manual
'''
This program is used for the sales person want to sale the product to customer
sales get the list price for the product, it is assumed the range is between maximum and minumum
only after the price is correct
the sales can keyin how many quantity he wants to sale
and then the computer show the total price
'''

maximum=20
minumum=15

list_price=int(input("Keyin the numeric data:"))
try:
    if (list_price > maximum or list_price < minumum):
        raise ValueError(list_price)
   
except ValueError as e:
    print (str(e)+ " your Input data is", str(e), "is wrong range between %d and %d!"%(maximum,minumum))
else:
    print ("input is right data")
finally:
    print("finally")

#any problem you find for real application
qty=int(input("the Quantity for order:"))
print ("the Total sale=",list_price*qty)


        
