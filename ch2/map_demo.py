#funcion: built-in function map

def func_twice(x):
    return x*2

listarray=range(1,10)
print("originl listarray is ",list(listarray))
result=[]
result=list(map(func_twice,listarray))
print("result of twice is",result)

#baseball pitcher Mr Chen           
chen_salary = [300,350,500,1200,1500]
times = [1.2,1.5,1.7,1.3,1.7]

chen_salary_2016=[]
chen_salary_2016=list(map(lambda x,y:x*y, chen_salary ,times))
print(chen_salary)
print(times)
print(chen_salary_2016)

