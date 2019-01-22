#filename: list_operation.py
#function: list operation

members_list = ["jack  Stahl", "Jack welhse","john Kenny","Johnny shieh"]

del members_list[0]   # index 0 from the list removed 
print (members_list) 
members_list.remove("john Kenny") # remove the john Kenny from the list, not the index 4
print ( members_list)

members_list.reverse()
print ( members_list)

members_list.pop(1)   # index 1 from the list removed
print ( members_list)

Listing = [6, 10,15,22,29,46]
print(Listing)
Listing.reverse()
print(Listing)


members_list.remove(members_list[0])
print ( members_list)
