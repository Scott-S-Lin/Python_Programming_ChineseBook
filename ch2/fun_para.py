
#filename: fun-para.py in chap2
#function: parameters maybe no, more, or arbitary parameters


def fun_return_data(a,b):
    c = a + b
    return c
def adding(*paras):
    total = 0
    for data in paras:
        total += data
    return total
print("\nplease input two data to Function")
data1=input()
data2=input()
data1=int(data1)
data2=int(data2)

total = fun_return_data(data1,data2)
print("return add use int is:",total)
total = fun_return_data(str(data1),str(data2))
print("return add use str is:",total)



print("pls input data3, and data4")
data3=input()
data4=input()
print('\n will call adding  function using Arbitary parameters\n')
print(adding(data1,data2))       
print(adding(data1,data2,int(data3)))     
print(adding(data1,data2,int(data3),int(data4)))  
