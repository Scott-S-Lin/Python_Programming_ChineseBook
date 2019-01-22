#filename: Create_zip.py
#function: create the Dict using {} and zip()


inventory_pn = ["11-1101", "11-1102", "51-1101"]
inventory_pn_stock = [1000, 30000, 200]

zip_pn=zip(inventory_pn,inventory_pn_stock)
print(set(zip_pn))

inventory=dict(zip(inventory_pn,inventory_pn_stock))

Partno = inventory.items()
# Loop and display tuple items.
print("   P/N      Stock")
print("-----------------")
for Pn in Partno:
    print(" ", Pn[0]," ",Pn[1])

