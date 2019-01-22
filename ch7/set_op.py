#filename:set_op.py
#functio:set operation 

#union is to merge two sets. 
s_Japan = set([34, 37, 38,37.5])
s_Usa = set([36, 37, 40,37.5])
s_union=s_Japan.union(s_Usa)
print(s_union)

#update adds a group of elements to a set.
s_union.update([39, 41, 42, 39.5])
print("s_union after update from other area=",s_union)


#big data anlysis
s_TPE = set([39, 36.5, 37, 37.5])
s_KS = set([37.5, 37, 39, 40])
s_TN = set([37, 39, 40, 37.5])
print("the common data =",set.intersection(s_TPE, s_KS, s_TN))


MBA10 = set(["Jake", "Johnny", "John"])
MBA11 = set(["Edward", "Mary", "John"])
print( MBA10.difference(MBA11))
#set(['Jake', 'Eric'])
print(MBA11.difference(MBA10))







