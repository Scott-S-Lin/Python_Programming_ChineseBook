
class Grandfather:
    money=2000
    lastname="Sun"

class father(Grandfather):
    money=100000
    firstname="CT"
    
class SonMultiDerived(father):
    print("SonMultiderived")
    nickname="Edward"
    amount=0
    amount=amount+Grandfather.money+father.money
  
Edward=SonMultiDerived()
print("Edward get the money from father and mother is\n ",Edward.amount)
print("Edward name is",Edward.nickname,Edward.lastname)
#print(SonMultiDerived.__mro__)
#print(SonMultiDerived.mro())
