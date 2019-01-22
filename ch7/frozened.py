#filename:frozened.py
#function: frozenset
#Frozenset. frozenset is an immutable set. We CANNOT add or remove elements.
#it cannot be changed, it can be used as a dictionary key
# initialize a frozenset with the built-in frozenset() function

keys = ["Johnny"]

# Create Set using frozenset
fset = frozenset(keys)
print(fset)

#try to add the Key to Frozened set, but CANNNOT add key in the Frozenset
try:
    print("Key in the new key to Frozened")
    Newkey=input()
    fset.add(Newkey)
except AttributeError:
    print("Cannot add")
    
    
# use frozenset as a key to dictionary.
diction = {}
diction[fset] = 12
print(diction)

# Dctionary contains key-value pairs.
dictionary = {"Johnny": 12, "John": 25, "Ted": 3}
print("Dictionary=",dictionary)

# This set contains only the dictionary's keys, not value
keys = set(dictionary)
print("Keys are=",keys)

