#filename:list-comp-create.py
#function:general list creation and list comprehension 

n=int(input("plese keyin in the range count to n for range(n):"))
doublelist = []

for x in range(n):
   doublelist.append(x*2)
print("doublelist is ",doublelist)


doublelist = []
doublelist = [x*2 for x in range(n)]
print("doublelist using list comprehension is ",doublelist)
