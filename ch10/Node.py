#filename:Node.py
#function: node class for storing the employee_no and salary

#node class 
class Node:
    
    def __init__(self):
        self.employee = None
        self.next = None     
      
    def setData(self,data,sal):
        self.employee = data
        self.salary = sal  
    
    def getData(self):
        return self.employee, self.salary    
    
    def setNext(self,next):
        self.next = next
     
    #get the next field of the node    
    def getNext(self):
        return self.next
