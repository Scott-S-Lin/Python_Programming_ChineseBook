#filename:Sensor_dict_del.py
#function:Sensor data using dict 

#Create a dictionary
Sensor_Hub1_data = {}

#Initialize value
Sensor_Hub1_data = {'S1':30,'S2':30,'S3':30}
print(Sensor_Hub1_data)


# Inserting/Updating value 

Sensor_Hub1_data['S1']=31 
Sensor_Hub1_data.update({'S2':31})
print(Sensor_Hub1_data)

# Deleting key in dictionary 

del Sensor_Hub1_data['S3'] 
print(Sensor_Hub1_data)
del Sensor_Hub1_data
print(Sensor_Hub1_data)




