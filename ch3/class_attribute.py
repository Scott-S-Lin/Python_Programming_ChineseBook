
class Class_attr: 
#class data is counter and class_fund
    counter = 0 
    class_fund=0
    
    def __init__(self):
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1

if __name__ == "__main__":

  Tang = Class_attr()  
  Class_attr.class_fund =Class_attr.counter*1000
  print("Number of instances: : ", Class_attr.counter)
  
  Big_David = Class_attr()
  Class_attr.class_fund =Class_attr.counter*1000
  print("Number of instances: : " + str(Class_attr.counter))
  
  del Big_David
  print("Number of instances: : " + str(Class_attr.counter))
  Class_attr.class_fund =Class_attr.counter*1000 
  print(Class_attr.class_fund)

