#filename: Chap_8_ex1.py
#function: create the Dict using {} and zip()
#question: how to fix the bug


inventory_pn = ["11-1101", "11-1102" "51-1101"]
inventory_pn_stock = [1000, 30000, 200]
inventory=dict(zip(inventory_pn,inventory_pn_stock))

Partno = inventory.items()
# Loop and display tuple items.
print("   P/N      Stock")
print("-----------------")
for Pn in Partno:
    print(" ", Pn[0]," ",Pn[1])

