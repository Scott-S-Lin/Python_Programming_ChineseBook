#filename:update.py

Year_end_set = {11,13}
#>>> my_set[0]
#TypeError: 'set' object does not support indexing
Year_end_set.add(22)
print(Year_end_set)

RD=[22,14,13]
Year_end_set.update(RD)
print(Year_end_set)

SW=[14,25]
Sales={11,16,18}
Year_end_set.update(SW, Sales)
#Year_end_set.update([14,25], {11,16,18})
print(Year_end_set)


Stringset = set('Mary')
print(Stringset)
Stringset.update('python')
print( Stringset)

Stringset.update([3,5], {1,9,8})
print( Stringset)
Stringset.add('Everybody Love')
print( Stringset)
