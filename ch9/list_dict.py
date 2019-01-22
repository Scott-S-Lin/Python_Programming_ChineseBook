#filename: list_dict.py
#function:The except error is useful for some application

listdata = [80,82,90,85,82,100,83,62,89,90,80,78,92,98,68,97,92] 
 
Engdict = {} 
 
for i in listdata: 
    try: 
        Engdict[i] += 1 
    except(KeyError): 
        Engdict[i] = 1 
print ("The Englisg score is ",Engdict)


key = Engdict.items()
max = 0
count=0
i=0
for k in key:
    i=i+1
    if k[0] > max:
       	max = k[0]
       	count=k[1]

print("English max=",max,"How many student count=",count)

print(i)
print(len(listdata))

#value = d.get(key, "empty")

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
       print ("division by zero!")
    else:
       print ("result is", result)
    finally:
       print ("executing finally clause")

       

def mode(list):
	
	d = {}
	for elm in list:
		try:
			d[elm] += 1
		except(KeyError):
			d[elm] = 1
	
	keys = d.keys()
	max = d[keys[0]]
	
	for key in keys[1:]:
		if d[key] > max:
			max = d[key]

	max_k = []		
	for key in keys:
		if d[key] == max:
			max_k.append(key),
	return max_k,max


