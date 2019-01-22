#filename:ifelse.py
#function:the If control

original_amount=50000
print("\n please key in the money")
withdraw = input()
withdraw=int(withdraw)
if withdraw <= 20000 and withdraw >0 :
   print ("The withdraw money is ",withdraw)
   original_amount -=withdraw
   print ("the current account money is",original_amount)
   
elif withdraw <= 30000:
   print ("the withdraw money is 30000")
   original_amount -=withdraw
   print ("the current account money is",original_amount)
else:
   print ("the withdraw is greater than 30000, Warning!!!!")

print ("have a niceday, Good bye!")
