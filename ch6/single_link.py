#filename:single_link.py
#function: single linked list

class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next
     
    #method for setting the data field of the node    
    def setData(self,data):
        self.data = data
      
    #method for getting the data field of the node   
    def getData(self):
        return self.data
     
    #method for setting the next field of the node
    def setNext(self,next):
        self.next = next
     
    #method for getting the next field of the node    
    def getNext(self):
        return self.next
 
class SingleList(object):
 
    head = None
    tail = None
 
    def showll(self):
        print ("Showing list data of linkedl:")
        current_node = self.head
        while current_node is not None:
            print (current_node.data, " -> ",end=" ")
            current_node = current_node.next
        print ("The end list is Nil ",None)
 
    def append(self, data):
        node = Node(data, None)
        print("Data is ",data)
        if self.head is None:
            print("The 1st node")
            self.head = self.tail = node
        else:
            print("Not the 1st node")
            self.tail.next = node
        self.tail = node
 
    def remove(self, node_value):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == node_value:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
 
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next
 
 
linkedl = SingleList()
linkedl.append(10)
linkedl.append(20)
linkedl.append(30)
linkedl.showll()

linkedl.remove(30)
linkedl.remove(20)
linkedl.remove(2)
linkedl.showll()
