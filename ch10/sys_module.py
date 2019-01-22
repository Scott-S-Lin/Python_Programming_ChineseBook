#filename:sys_modudle.py (in chap10)
#function: using the sys.modules to know which modules have beed loaded

import sys
import fibo
print("***The following modules are impoerted:\n")

print(sys.modules)

#print("\n Module names are\n")
select=input("\nwhich module name you want to find:")

for module_name in sys.modules:
    if module_name== select:
        print("*****MODULE name %s is loaded="%module_name)


if fibo in sys.modules:
    print("@@@@@ Fibo is loaded @@@@")

print("***How many modules are loaded:\n")
print(len(sys.modules))
print("\nsystem verion is :",sys.version)
print("\nsystem platform is:",sys.platform)
      
