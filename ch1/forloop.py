#filename:forloop.py
#function: the for loop function

for char_var in 'UCB':     
   print('chracter is', char_var)

brands = ['Apple', 'Samsung', 'IBM', 'Asus']
for br in brands:    
   print('Brand fan :', br)
   
total=0
stud_scores =[95,80,75,98,70,85]
for stud in stud_scores:
    total+=stud

number = len(stud_scores)
print(number)
print("average of scores is" ,total/number)

"""please also check with 1.4.5 string_method.py and compare if the purpose is
same """
message_text = 'coap protocol for some IoT projects'
print("\nthe char count is ",message_text.count('o'))
text_count =message_text.count('o')

count=0
for char_o in message_text:
 if char_o =='o':
  count +=1
print('total o is',count)

if count==text_count:
    print("congratulation, your programming skill is good enough")
print("\n\nGood bye!  program will exit")
import sys
sys.exit()
