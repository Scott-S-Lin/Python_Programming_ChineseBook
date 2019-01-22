#filename:stacking.py
#funcion: define _init_ using the empty list first
#push the items in the stack ... and so on

class Stack:
    def __init__(self):
        print("_init_ is doing")
        self.items = []
         
    #method push purpose is to push items
    def push(self,item):
        self.items.append(item)
         
    #method pop 
    def pop(self):
        if len(self.items)==0:
            raise ValueError('should have data in stack first')
        else:
            return self.items.pop()
     
    #isempty method is to check if stack is empty
    def isempty(self):
        return (self.items == [])
     
    #method to check how many items in the stack
    def countofstack(self):
        return len(self.items)
     
    def __str__(self):
        return str(self.items)
     
 
if __name__ == "__main__":

    stackobj = Stack()
   # print( stackobj)
   # stackobj.pop()
    
    stackobj.push("Johnny")
    stackobj.push("score")
    print( stackobj)
        
    stackobj.pop()
    print(stackobj)
         
    print ("the items count of stack is", stackobj.countofstack())
    
