#filename: func_multi_ret.py
#funcion: declare functions, receiving a variable number of arguments, using the *
#function: return multi result from the function

def multi_variable(var1, var2, *others):
    print ("var1: %s" % var1)
    print ("var2: %s" % var2)
    print ("others: %s" % list(others))
    
multi_variable(483.5,450.7,350,410,420,410,320)


#2015 university examination for medical school 
def return_multi(score1, score2, score3):
    if score1 >=450.7:
        school_a="NTU medical ok"
    if score2 >=443.5 :
        school_b ="yangmin medical"
    if score3 >=442:
        school_c= "chenkung medical"
    return school_a,school_b,school_c
 
print("\nmulti-return from the function")
ret_school = return_multi(483.5,443.5,446)
for i in ret_school:
    if i:
        print("\t",i)
