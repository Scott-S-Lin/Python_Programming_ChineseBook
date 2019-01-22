#filename:ch6_bs_sorted.py
#function: binary search after the listis sorted
# Python3.x.x version .codes
#1: create a list
#2: sort the list
#3: binary search algorithm based on the Book description Step1,2,3
 
import random
 
pivot = 8                    # number to search for
size = 10                   # size of random array
elements=[]

#generate the random list, 1. Create a list
i=0
while i<size:
    data=random.randint(0,30)
    elements.append(data)
    i+=1
    
#sort the elements, 2. Sort the list
elements = sorted(elements)
print(pivot, elements)      # The data has been sorted , and the Key we want
 
# Binary Search for number in array based on the step1,2,3 in the Book
def binary_search(key, listing, low, hi):
    if hi < low: return -1       # not found and  more numbers
    mid = (low + hi) // 2        # Rmid is the midpoint of list
    if key == listing[mid]:
        return mid               # Key is found here
    elif key < listing[mid]:
        return binary_search(key, listing, low, mid - 1)   # try left of list
    else:
        return binary_search(key, listing, mid + 1, hi)    # try Rigth of list
 
def searching(sentiel, array):     # searching the Key (Sentiel)
    return binary_search(sentiel, array, 0, len(array) - 1)

#search the pivot Key using the binary search,
#the pivot is generated using randomint

global pivot
pivot =random.randint(0,30)
print("the Pivot we want to search is  ",pivot)
RmIndex = searching(pivot, elements)
if RmIndex < 0:
    print("not found the data")
else:
    print("Data is found at index", RmIndex)
