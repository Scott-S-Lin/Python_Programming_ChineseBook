#filename:list_create.py
#function:list creation

#Creat list using []
newList = []
print("newLIst=", newList)

for i in range(0, 5):
   newList.append(i*2)
print("newlist after using append()=",newList)

#create list using list()
outputlist=list()
print("Outputlist=",outputlist)
for x in newList:
   if x%2 == 0:
     outputlist.append(x)
print("outputlist after using append()=",outputlist)

#create list using list comprehension
output=[]
print("Ouput=",output)
output = [x for x in newList if x%2 == 0]
print("output after using list comprehension=",output)

#output
#newLIst= []
#newlist after using append()= [0, 2, 4, 6, 8]
#Outputlist= []
#outputlist after using append()= [0, 2, 4, 6, 8]
#Ouput= []
#output after using list comprehension= [0, 2, 4, 6, 8]


