
#Filename: module_example.py
#function: define function and variables

salesweight = 10
YYMMDD = 20160221
print("--->>>>module_example.py is executing, The  prgram module is %s"%__name__)

# define some functions
def print_start():
    print ("The fruit is ok for 2016 sale")    
   
class Fruit:
    def __init__(self):
        
        self.type = input("What type of fruit? ")
        self.weight = int(input("What weight (in g)? "))
        self.price = input("How much per g ? ")
        self.when = input("When the fruit will output from Hwanen? ")  
       
   
    def printdata(self):
        print ("\nthis year fruit is about " + str(self.weight) + " g",)
        print (self.type, "fruit ", "MMDD:" +self.when, " costing/g is:" + self.price + " NTD.")


