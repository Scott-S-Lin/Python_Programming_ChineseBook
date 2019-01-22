#filename:remove.py
#function:remove and discard method, which are used to delete the element of set

Spring_EE_CS_course = {3101,3106,3210}

Database=[5101,5106]
Spring_EE_CS_course.update(Database)
print(Spring_EE_CS_course)
if len(Spring_EE_CS_course) >4:
    print("\ntoo many course for one semester")
    print("please remove one course")
    print("your courses are", Spring_EE_CS_course)
    print("please keyin one course from your current course")
    dis_course=int(input())
    Spring_EE_CS_course.discard(dis_course)
    
print(Spring_EE_CS_course)    

PHD=set(['IOT IPV6', 'VLSI', 'Business strategy', 'WSN'])
PHD.remove('IOT')
print(PHD)


