#filename:ex6-3.py
#funcion: annual party game

listresult = []
for basis in [10,30,50]:
 for times in [2,3]:
  listresult.append(basis*times)
	
print(listresult)


listresult=[]
listresult=[basis*times for basis in [10,30,50] for times in [2,3]]
print(listresult)


            
