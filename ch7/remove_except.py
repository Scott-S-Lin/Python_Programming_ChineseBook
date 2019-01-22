#filename:remove_except.py

Allien= set(range(20))
OIC = set(range(1,5))
print("Allien set=",Allien)
print("OIC set=",OIC)

Allien.discard(OIC)
print("Bigger set=",Allien)
#try:
 Allien.remove(OIC)
