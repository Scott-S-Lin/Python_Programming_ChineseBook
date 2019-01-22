#filename:Get_len.py
#function: get the key and we can know the value
Smartphone_cost = {"11-1101": 800, "11-1102": 600, "12-1101": 650}
keys = Smartphone_cost.keys()
cost = Smartphone_cost.values()

print("Keys:")
print(keys)
print(len(keys))

print("Values of cost:")
print(cost)
print(len(cost))

# Create list of tuple pairs.
# ... These are key-value pairs.
Smartphone = [("11-1101", 30000), ("11-1102", 40000), ("12-1101", 20000)]
# Convert list to dictionary.
Dbase = dict(Smartphone )

# Test the stock_money in dictionary.
part_no="11-1101"
if (Dbase.get(part_no)):
    print("Key %s is found"%part_no)
    print(Dbase.get(part_no))
print("total Product has %d kind of stock"%len(Dbase))
print("need sell the high stock product")


