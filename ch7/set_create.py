#filename:set_create.py
#filename: using name={"data1","data2".....} to cretae the Set

# Create a set.
members = {"Johnny", "CC Tsai", "Johnny", "John", "Edward"}
Top_ceo = {"Stan","Johnny","CC","Simon","John"}

print(members)
print("Member length is ",len(members))

# Search members from the set using keyword in.
print("Please key in the Name you want to search")
search_member=input()
if search_member in members:
    print(search_member,"  found in the member set")
else:
    print(search_member,"  not found in the member set")

#Search members from the set using keyword not-in.
print("Please key in the Name you want to Add")    
search_member=input()
    
if search_member  not in members:
    print(search_member,"  not found in the member set")
    members.add(search_member)

print(members)
print("Member length is ",len(members))
