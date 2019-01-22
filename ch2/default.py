
#filename:default.py
#function:default parameters

def calculate(NCCUa, NCTUb, NCCUc=0, NCTUd=0):
    print("4 data=",NCCUa, NCTUb, NCCUc, NCTUd)
    return NCCUa -NCTUb + NCCUc -NCTUd

Groupa=calculate(72,75)
print(Groupa)

Groupb=calculate(78,82,NCTUd=1)
print(Groupb)

Groupc=calculate(82,80,1,0)
print(Groupc)

Totalscore=Groupa+Groupb+Groupc
print(Totalscore)
