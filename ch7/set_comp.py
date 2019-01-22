#filename: set_comp.py
#function : set comprehension

print("please keyin the choice from YyNnEe")
rawdata=input()
#a = {x for x in 'abracadabra' if x not in 'abc'}
a = {k for k in rawdata  if k not in 'YyNnEe'}
print("the final data after set comprehension =",a)

#create a set first and use the set comprehension 
Keylist ={"John","Edward","Johnny", "Steve","CT"}
Finalkeylist={item for item in Keylist if item is not "Johnny"}
print("final ketlist =",Finalkeylist)

      
