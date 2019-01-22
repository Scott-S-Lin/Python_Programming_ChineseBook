#filename:Multi-inherit.py (in chap 4)
#function: multi derived class function, and the Method resoluyion Order(MRO)
#is Depthe first and left-right search

#MRO :the method resolution order for classic classes in python
#is described as a depth-first left-to-right search
class SuperClass(object):
    def __init__(self):
        print ("Initialized SuperClass")

class father(SuperClass):
    
    def test():
        print ("Initialized father")

class mother(SuperClass):
    
    def __init__(self):
        print ("Initialized mother")

class DepthFS(father, mother):
    money=0
    def __init__(self):
        super(DepthFS, self).__init__()
        print ("Initialized DepthFirtssearch")

print(DepthFS())
#The MRO use the concept of DFS, that is MRO rule 
#super(DFS, self).__init__() looks for an __init__ method in the first class
#in self.__class__.mro() after DepthFS. Since father does not have an __init__,
#it then looks for an __init__ method in mother.
#It finds mother.__init__, and therefore calls mother.__init__(self).
print(DepthFS.mro())
