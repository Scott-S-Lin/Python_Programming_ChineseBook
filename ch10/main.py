
#filename: main.py
#function: import module
#USING AN IMPORTED MODULE, sytax format is modulename.itemname
#usage :  modulename.function_name()
#usage :  modulename.variable

import module_example
year_weight=0

print("Main .py execution ,The  prgram module is %s"%__name__)

print (module_example.print_start())
print ("fruit ouput on :",module_example.YYMMDD)


print("class init")
try:
   CSAfruit = module_example.Fruit()
   module_example.salesweight = CSAfruit.weight
   year_weight+= CSAfruit.weight
   CSAfruit.printdata()
except ImportError as e:
   print("something wrong",str(e))

print("year sale weight=",year_weight)

if __name__ == "__main__":
    print("The main prgram is %s"%__name__)
