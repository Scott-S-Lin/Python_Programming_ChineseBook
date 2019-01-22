#filename:ex6-1-ls-bs.py
#funcion : test the linear search and binary search performance

import random
import sys

#the following code is for reference
listing=[]
size=16
i=0
while i<size:
    data=random.randint(0,20)
    listing.append(data)
    i+=1
print(listing)
#listing1 = sorted(listing)
    
def linear_search(item):
    
    listing = [4,8,45,24,18,32,9,46,3,23,29]
    searchPass = 0

    for Km in listing:
        searchPass += 1
        if Km == item:
              print ('Pass counts using linear search is ',searchPass)
              return

    print (str(item),'not found the search item')

linear_search(9)


#binary search after the Data is sorted
#the time complexity of binary search is as follows (my see my BCC book)
#best case:o(1)
#worst case: o(log2(N))
"""
To determine how many Pass are examined in a list of size n
"""
def bisearch(item):
     listing1 = [3,4,8,9,18,23,24,29,32,45,46]
     print(listing1)
     
     
     searchPass = 0
     low = 0
     high = len(listing1)-1
     mid = int((high + low)/2)
     searchPass += 1 # already divided list in half at this time
     while listing1[mid] != item:
         if  listing1[mid] < item:
             low = mid + 1
         else:
             high = mid
         mid =int( (high + low)/2)
         searchPass += 1 
     print ('Pass counts using Binary search is ',str(searchPass))

print("Binary search")
bisearch(9)

#program output
#[17, 20, 9, 4, 12, 7, 0, 9, 10, 6, 2, 16, 9, 4, 2, 17]
#Pass counts using linear search is  3
#Binary search
#[0, 2, 2, 4, 4, 6, 7, 9, 9, 9, 10, 12, 16, 17, 17, 20]
#Pass counts using Binary search is  1
