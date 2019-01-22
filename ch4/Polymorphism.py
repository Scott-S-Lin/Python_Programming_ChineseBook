#filename:Polymorphism.py
#function:Object oriented's feature Polymorphism


import datetime
nowtime = datetime.datetime.now()
#print (str(nowtime))

class Mother:
    message=0
    def __init__(self, name):    
        self.name = name
    def sendmessage(self):             
        raise NotImplementedError("Need abstract method")

class Sister(Mother):
    def sendmessage(self):
        Mother.message+=1
        return 'Mama , I love you'

class Brother(Mother):
    def sendmessage(self):
        Mother.message+=1
        return 'Hi! Ma        '

second_gen_persons = [Sister('Mary'),Sister('Jessica'), Brother('Carl')]

for person in second_gen_persons:
    nowtime = datetime.datetime.now()
    print (person.name + ': ' + person.sendmessage()+ " at "+str(nowtime) )
    
print("message from mother's son and daughter is on mm/dd ","%d %d"%(nowtime.month,nowtime.day))

print("total message from her son and duagther is ", Mother.message)
