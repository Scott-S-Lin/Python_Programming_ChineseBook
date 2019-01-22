#filename:employ1.py in chap4
#function:the derived class funcion 
class Person:
    def __init__(self, first, last, field):
        self.firstname = first
        self.lastname = last
        self.field = field
        
#__str__ is a special method, like __init__
#used to return a string representation of an object.
    def __str__(self):
        return self.firstname + " " + self.lastname + ", " + str(self.field)

#object.__repr__(self): called by the repr() built-in function and by string conversions (reverse quotes)
#   to compute the "official" string representation of an object.
#object.__str__(self): called by the str() build-in function and by the print statement to compute the "informal" string representation of an object.
#   From the official documentation, we know that both __repr__ and __str__ are used to "represent" an object.
#__repr__ should be the "official" representation while __str__ is the "informal" representation.
    
    def __repr__(self):
        return repr((self.firstname, self.lastname, self.field))


#the derived class derive from Person class
class Employee(Person):
    def __init__(self, first, last, field, employee_no):
        super().__init__(first, last, field)
        self.employee_no =employee_no

    def __str__(self):
        return super().__str__() + ", " +  str(self.employee_no)
    def __repr__(self):
            return repr((self.name, self.grade, self.score))

Person_objects = [
    Person('john ', 'Peng', "Linux"),
    Person('jennis', 'shen', 'Account'),
    Person('jocelym ', 'Tsai', 'Sales'),
]
Employee_objects = [
    Employee('john ', 'Peng', "Linux",15),
    Employee('jennis', 'shen', 'Account', 420),
    Employee('jocelym ', 'Tsai', 'Sales',520),
]
x = Person("Robert", "Dineno", "Actor")
y = Employee("Jeff", "Lin", "Computer SW", 2)
print("The super class string description:\t",x)
print("The derived class string description:\t",y)
#print("The derived class string description:\t",Person_objects)
print("sort the data by the key of field from top to low")
print(sorted(Person_objects, key=lambda Person:Person.field, reverse=True))



