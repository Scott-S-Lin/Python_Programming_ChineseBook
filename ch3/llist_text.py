
#filename:llist_text.py
#function: build linked list

class Node:
  def __init__( self, data ):
    print("init node")
    self.data = data
    self.next = None
    

class LinkedList:
  def __init__( self ):
    print("Init List")
    self.head = None
    self.tail = None

  def Add( self, data ):
      print("Node data=",data)
      newnode = Node( data )

      if self.head == None:
        self.head = newnode
      if self.tail != None:
        self.tail.next = newnode

      self.tail = newnode
  
  def PrintList( self ):
      node = self.head
      while node != None:
        print (node.data)
        node = node.next
    
LList = LinkedList()
LList.Add("John")
LList.Add("Johnny")
LList.Add("CT")
print("The linked list is ")
LList.PrintList( )


