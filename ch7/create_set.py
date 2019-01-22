
#filename:cteat_set.py
#function:create set and add the temperature using add method
#get the temperature from the sensor and add to set

import sys

    
temper_sensor=set()
temper_sensor.add(38)
temper_sensor.add(36)
print("temper_sensor=",temper_sensor)

IOT_temp_area2_in_TPE = {28, 31,30,32, 39, 37.5, 38}

# Union the sets from two Sets data
IOT_set_TPE = temper_sensor.union(IOT_temp_area2_in_TPE)
print(IOT_set_TPE)

abnormal_set = {k for k in IOT_set_TPE  if k > 37.5}
print("abnormal data  after anlyzing the IOT data about the temperature =",abnormal_set)



isempty = len(abnormal_set)      # Test for emptiness
if isempty ==0 :
    print("no abnormal case")
    sys.exit()
else:
    print("we should try to exceute some detailed analysis")
    pass
#   pass_2_cloud("google.ocm",12,"POST")

    

#evaluate the Set data for IOT category
IOT_category={"Car","stores","agriculture","fish","medical"}
print("iot category =",IOT_category)


