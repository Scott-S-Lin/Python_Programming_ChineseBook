#filename:staticmethod.py
#funcion:specail methods of Python

#@staticmethod means: when this method is called,
#indeed, no need to pass an instance of the class to it , we(as we normally do with methods).
#This means you can put a function inside a class
#No need to have a instance .but you can't access the instance of that class (this is useful when your method does not use the instance).
# We no need to have a instance, we can use classname.Methodname() to access
#@classmethod means: when this method is called
#use class as the first argument instead of instance of that class (as we normally do with methods).
#This means you can use the class and its properties inside that method rather than a particular instance.

#@staticmethod: no need the slef and the class cls parameter , use it like the function way。
#@classmethod: noe need the self parameter, but the first parameter need to use cls, which means the cls parameter。


class StaticClass(object):  
    count = 0
    def forking(self):  
        print ('forking')  
 
    @staticmethod  
    def static_way():  
        print ('static_way')  
        print (StaticClass.count)
        StaticClass.count +=1
#cls().forking()
#NameError: name 'cls' is not defined    
        
    @classmethod  
    def class_way(cls):  
        print ('class_way')  
        print(cls.count )
        cls.count +=1
        cls().forking()
        
StaticClass.class_way()	  
StaticClass.static_way()  
StaticClass.class_way()  
