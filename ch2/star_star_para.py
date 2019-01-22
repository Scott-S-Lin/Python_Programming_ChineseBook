#filename:star-star-para.py
#function:try to understand the ** parameter from the IOT(internet of thing) device
#to get the temperature

def func_formal(p1,p2,p3,p4):
    total=p1+p2+p3+p4
    print("total=",total)  
func_formal(36,38,*range(2))

def subprogram(temp, **kws):
    print ("\ntemperature", temp)
    for key in kws:
        print ("other temperature is: %s: %s" % (key, kws[key]))

subprogram(temp=36, arg2=38, arg3=36.5)


def subroutine(arg1, arg2, arg3):
    print ("\npara1:", arg1)
    print ("para2:", arg2)
    print ("para3:", arg3)
    total=arg1+arg2+arg3
    print("total=",total)

kw_dict = {"arg3": 38, "arg2": 36, "arg1":39.5}
subroutine(**kw_dict)

