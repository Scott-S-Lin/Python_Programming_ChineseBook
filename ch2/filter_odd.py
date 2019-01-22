#filename:filter_odd.py

ori_list = [13, 25, 22, 6, 18, 33, 23, 32]
new_list = list(filter(lambda x: (x%2 == 0) , ori_list))
print(new_list)


