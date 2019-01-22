#filename: Create_sort.py
#function: create the Dict and sort the key and print


Inventory = {"11-1101": 1000, "11-1102": 20006, "51-1101": 300}
# Sort the keys from the dictionary.
keys = sorted(Inventory.keys())
print(keys)

Partno = Inventory.items()
# Loop and display tuple items.
print("   P/N      Stock")
print("-----------------")
for Pn in Partno:
    print(" ", Pn[0]," ",Pn[1])

