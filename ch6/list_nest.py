
#filename:list_nest.py
#function: List ,It is possible to nest lists
# it menas list can create lists containing other lists

mem_list_USA_UK = ['adeile', 'Madonld', 'Elton John']
mem_list_TWN = ['fiev may','A-mei','five hundred']
global_singer = [mem_list_USA_UK,mem_list_TWN]
print("\nGlobal singer: ",global_singer )
print("USA UK singers:  ",global_singer[0] )
print("USA UK singers no 1 ",global_singer[0][0])

