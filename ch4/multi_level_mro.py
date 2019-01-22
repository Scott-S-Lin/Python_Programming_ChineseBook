#filename:multi_level_mro.py in chap4
#function: the MRO depth first search rule study, and multiple inheritane concept
#MRO of a class can be viewed as the __mro__ attribute or mro() method.
#The former__mro__ returns a tuple, while latter  mro()  returns a list.

class Grandfather:
    money=2000

class father(Grandfather):
    money=100000
    
class SonMultiDerived(father):
    amount=0
    amount=amount+Grandfather.money+father.money
  

Edward=SonMultiDerived()
print("Edward get the money from father and grandfather is\n ",Edward.amount)

print(SonMultiDerived.__mro__)
print(SonMultiDerived.mro())



