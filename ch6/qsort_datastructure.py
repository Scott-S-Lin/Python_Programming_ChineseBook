#filename:qsort_datastruture.py(in chap6)
#function: quick sort Data structure using Python , the algorithim is very importanta 


import random
from random import randrange

listdata=[]
elements = []

def quicksortele(list1):
    if list1 == []:
        return []
    else:
        pivot = list1[0]
        lesss = quicksortele([x for x in list1[1:] if x < pivot])
        greats = quicksortele([x for x in list1[1:] if x >= pivot])
        return lesss + [pivot] + greats
    
def qsort_list_comprehension(listdata):
    if len(listdata) <= 1:
        return listdata                                                                                     
    pivot = listdata[0]
    restlist = listdata[1:]
    smaller = [n for n in restlist if n <= pivot]
    larger = [n for n in restlist if n > pivot]
    return qsort_list_comprehension(smaller) + [pivot] +qsort_list_comprehension(larger)

import time
elements=[]
i=0
while i<10:
    data=random.randint(0,20)
    elements.append(data)
    i+=1
start = time.clock()
print("before quicksortele",elements)
elements=quicksortele(elements)
print("after quicksortele",elements)
print(elements)
stop = time.clock()
print("compute time is", stop-start)
compute=stop-start

elements1=[]
i=0
while i<10:
    data=random.randint(0,20)
    elements1.append(data)
    i+=1
start = time.clock()
print("\nbefore quicksort",elements1)
elements=qsort_list_comprehension(elements1)
print("after quicksort",elements1)
print(elements1)
stop = time.clock()
compute_list=stop-start
print("compute time is using list comprehension:", stop-start)
print("\nthe speed difference is  percent",(compute-compute_list)/compute*100)

 
