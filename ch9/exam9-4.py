#filename:chap_ex5_average_except.py
#function: using reduce for total
#except can be applied to the wrong input data

englistdata = [80,82,90,85,82,100,83,62,89,90,80,78,92,98,68,97,92,"92"]
total=0

def score_sum( eng ):
   
    sum= 0
    for data in eng:
        sum += data
    return sum


try:
    total=score_sum(englistdata)
except TypeError:
    print("add Non-Numeric Data")
else:
    print("total=",total)
    

ave=score_sum(englistdata)/len(englistdata)
print("average=%3.2f"%ave)

