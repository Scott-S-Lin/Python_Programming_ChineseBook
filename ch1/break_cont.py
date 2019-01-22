#filename:break-cont.py
#function:you can use the break statement to jump out of the loop.
""" break : skip the while or for loop
    continue: to the next loop
"""
message=""
print("pls key in data until you keyin end")
while True:
    line = input('> ')
    if line == 'end':
        break
    print(" line=", line)
    message = message +line 

print("message is:", message)

for letter in message:     
   if letter == 'h':
      continue
#jump to next loop     
   print ('Letter :', letter)

