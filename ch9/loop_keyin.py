#filename: loop_keyin.py
#function: While loop for waiting the correct choice

print(" The ATM operation")
print("\n1. The Money transfer")
print("\n2. The deposit money")
print("\n3. The draw money")

while True:
  try:
      x = int(input("\nPlease enter a number of ATM choice: "))
      break
  except ValueError:
      print ("You keyin the wrong choice.  Try again...")
  except KeyboardInterrupt:
      print ("Pls don't press CTRL_C.  Try again...")
  except EOFError:
      print("EOF when reading a line, try again...")
