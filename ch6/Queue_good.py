#filename:Queue_good.py
class Node(object):
  def __init__(self, item = None):
    self.item = item
    self.next = None
    self.previous = None


class Queue(object):
#creates an empty FIFO queue    
  def __init__(self):
    
    self.length = 0
    self.head = None
    self.tail = None

#adds item at back of queue
  def enqueue(self, item):
    newNode = Node(item)
    newNode.next = None
    if self.head == None:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = newNode
      newNode.previous = self.tail
      self.tail = newNode
      
    self.length += 1
#    print("len=", self.length)

#if self.size() > 0
#removes returns the front item  
  def dequeue (self):
     if self.size()>0:
        item = self.head.item
        self.head = self.head.next 
        self.length = self.length - 1
        if self.length == 0:
          self.last = None
        return item

#if self.size() > 0 returns first item    
  def front(self):
    
    return item[0]

#returns the count of itemes in queue
  def size(self):
    return self.length
    

q=Queue()
q.enqueue('a') 
q.enqueue('b') 
q.enqueue('c')
print (q.size())
print (q.dequeue())
q.enqueue('d') 
print (q.dequeue())
print (q.dequeue()) 
print (q.dequeue()) 
print (q.dequeue())



