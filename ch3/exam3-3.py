#filenme:exam3-3-Employee.py
#function : class variable and class attribute 

class Employee:
   """
   Class Doc show the class attribute
   """
#Count is class variable
   Count = 0

   def __init__(self, name, no, salary,level):
     
      self.name = name
      self.no = no
      self.salary = salary
      self.level = level
      Employee.Count += 1
   
   def displayEmployee(self):
      print("-"*45)
      print ("No : ", self.no,  ", Salary: ", self.salary,", Level: ", self.level)

print ( Employee.__module__)
#if __name__ == "__main__":
   
John= Employee("John", "126",52000,"Engineer")
Ted = Employee("Teddy","34", 65000,"Manager")

print("Object ID ",id(John),"  ",id(Ted))
del Ted
print("Object ID ",id(John),"  ",id(Ted))
