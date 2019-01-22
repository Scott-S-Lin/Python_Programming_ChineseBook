#filename:linked_list_import.py
#function: Singly Linked List function
#we should create the node of a Singly Linked List, node class isimported from node module
#We use the import way like from random import randint 

#import random 
from random import randint
import Node
 
#Linkedlist class
class LinkedList(Node.Node):    
    def __init__(self):
        self.head = None
        self.length = 0
     
    #set head of Linked List
    def setHead(self,head):
        self.head = head                
     
    def insertHead(self,data,sal):
        newNode = Node.Node()
        newNode.setData(data,sal)
       
        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.length += 1
     
    #insert a new node at the end   
    def insertTail(self,data,sal):
        newNode = Node.Node()
        newNode.setData(data,sal)
               
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
             
        current.setNext(newNode)
        self.length += 1
     
                  
    #print the linked list of employee data
    def printList(self):
        current = self.head
        print("\n****print linked list****")
        print("Employee no      Salary")
        print("-----------------------")
        while current != None:
            print("\n\t%4s \t %6d"%current.getData(),end=' ')
            current = current.getNext() 
        print("\n-----------------------")
        
if __name__ == "__main__":
    linkedl = LinkedList()

try:
    employee_no=randint(0,300)
    print(employee_no)
    linkedl.insertHead(employee_no,80000)
    employee_no=randint(0,300)
    print(employee_no)
    linkedl.insertTail(employee_no,80000)
    employee_no=randint(0,300)
    print(employee_no) 
    linkedl.insertTail(employee_no,80000) 
    linkedl.printList()
except ImportError:
    import sys
    sys.exit()
else:
    print("\n\nprogram run normally, excellent")
finally:
    print("program finally")


    
