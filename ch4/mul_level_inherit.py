#filename : mul-level-inherit.py
#function: the multi-level inheritance 
#Consider this - a base class Grandfather, class father inheriting from Grandfather, class son inheriting from Grandfather.
#This is to show What is a generic way to invoke your parent class constructor in a constructor
#you can study the _init_ and Mro from the example
#_init_ is like the way of C++ constructor

class Grandfather(object):
    def __init__(self):
        print ("Constructor Grandfather was called")
        

class father(Grandfather):
    def __init__(self):
        super(father,self).__init__()
        print ("Constructor father  was called")
        

class son(father):
    def __init__(self):
        super(son,self).__init__()
        print( "Constructor son was called")
        

Edward =son()
print(son.__mro__)
print(son.mro())
