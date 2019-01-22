#filename:Pop-format.py
#function:remove and discard method, which are used to delete the element of set

Spring_EE_CS_course = {3101,3106,3210}
original = set(Spring_EE_CS_course)

Database=[5101,5106]
Spring_EE_CS_course.update(Database)
print(Spring_EE_CS_course)

if len(Spring_EE_CS_course) >4:
    print("\ntoo many course for one semester")
    print("please remove one course")
#    print("your courses are", Spring_EE_CS_course)
    print("please keyin one course from your current course")
    dis_course=int(input())
    Spring_EE_CS_course.discard(dis_course)
    
#print(Spring_EE_CS_course)

random_choose=Spring_EE_CS_course.pop()
print("random choice course is ",random_choose)
print("final courses are  ",Spring_EE_CS_course)

print("I choose original course {0} and finally are {1} ".format(original,Spring_EE_CS_course))

Spring_EE_CS_course.clear()
print("\n after clear() is executed the set is  ",Spring_EE_CS_course)
random_choose=Spring_EE_CS_course.pop()

#PHD course set 
PHD=set(['IOT IPV6', 'VLSI', 'Business strategy', 'WSN'])
print("PHD cousre is  ",PHD)

#use try except
#to avoid the program execution is stopped because of the KeyError
try:
   PHD.remove('IOT') 
except KeyError:
   print ("No IOT to remove")




