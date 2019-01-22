#filename: person.py
#function: use _init_ to create the Attribute of object

class person:
   def __init__(self, name,age,edu,hobby):
      self.name = name
      self.age = age
      self.education=edu
      self.hobby=hobby

John_Pan = person('John',35,"University","Golf")
Lucy = person('Lucy',32,"Master","joggling")

print (John_Pan.name,John_Pan.age,John_Pan.education,John_Pan.hobby)
print (Lucy.name,Lucy.age,Lucy.education,Lucy.hobby)
