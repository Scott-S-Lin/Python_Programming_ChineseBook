#filenme:Employee.py
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

#if __name__ == "__main__":
   
John= Employee("John", "126",52000,"Engineer")
Ted = Employee("Teddy","34", 65000,"Manager")
if hasattr(John, 'name') :
    John.displayEmployee()


setattr(Ted, 'salary', 68000)
Ted.displayEmployee()
print("Total Employee no is ",Employee.Count)


print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)
