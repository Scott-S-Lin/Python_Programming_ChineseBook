#filename:listex.py
#function: create the empy list, list can contains different data type

a=list()
print(a)
listex = ['中文', '日文','English', 6, [29,23,18,5,19,12]]
print (listex)
listex.append(8)
print (listex)
listex.extend(['1', '2', '3'])
print (listex)

elements = []
string = "I am a Python fan"
print("sring is: ", string)

for v in string:
#  print(v)
  if v == ' ':
      continue
  elements.append(v)
print(elements)
