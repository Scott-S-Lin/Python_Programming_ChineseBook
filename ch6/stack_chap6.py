#filename:stack_chap6.py(in chap6)
#function:using the list to provide the Data structure(ex. stack..)
#you can refer to  my C++ book , stack.cpp
#stack is a data structure that use the rule of last in first out (LIFO)
# it is used for kenerl for process
#refer to: tThe design of the unix operating system authored by MAurice J. Bach
#Queue is a data structure that use the rule of first in first out(FIFO)

import random

class Stack:
    def __init__(self):
        print("\n....init...")
        self.memberitems = []
         
    #using append() for pushing an item on a stack at the end
    def push(self,data):
        self.memberitems.append(data)
         
    #using pop() for popping an last item 
    def pop(self):
        return self.memberitems.pop()

    def countOfStack(self):
        return len(self.memberitems)
     
    #use return if self.objname is empty to check if list is empty
    def isEmpty(self):
        return (self.memberitems == [])
            
    def __str__(self):
        return str(self.memberitems)
     
 
if __name__ == "__main__":
    proc_stk = Stack()

if proc_stk.isEmpty() is True:
    print("stack is empty")
    i=0
    while i < 5:    
        proc_stk.push(random.randint(0,20))
#       print("id of member is",id(proc_stk(i)))
        i +=1

print ("the stack data is",proc_stk)
print("the stack id is",id(proc_stk))
   
proc_stk.pop()
print("stack count is",proc_stk.countOfStack())

    
