#filename:Whileloop.py
#function: test while loop, the starting and max no is keyined via KB
#filelocation: d:\book\chap1

total=0
count = 0
print("pls keyin the max no")
max=int(input())
print("pls keyin the staring no")
count=int(input()) #input data from Keyboard


while (count < max):    
   print ("The count is:", count,end="   ")
   total   = total + count
   count = count + 1
   print("while block")
          
print ("total is ",total)
