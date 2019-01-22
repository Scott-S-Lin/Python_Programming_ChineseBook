#filename:chap10_ex1_reload_mod.py
#function:using the format reload(sys.modules['module'])
#import the module of sensor hub data and function, the module name is sensor_hub


from importlib import reload
import sys
import sensor_hub
import time
#from time import sleep

t_mod=input("sensor hub module:")

alreadymodule = sorted(sys.modules.keys())
#print("\n Alreadymodule :", alreadymodule)

if t_mod in alreadymodule:
    print("module %s is in the already imported list"%t_mod)
    reload(sys.modules[t_mod])
    while True:
        print("\nThe rule of data has been changed to ",sensor_hub.sec)
        print(sensor_hub.sensor_degree)
        current_degree=int(input("pls input the current degree:"))
        test=sensor_hub.sum_data(current_degree,sensor_hub.previous_degree)
        print("\n test degree is :",test)
        print("\n waiting ")
        time.sleep(sensor_hub.sec)
        sensor_hub.previous_degree=current_degree
        if test in sensor_hub.sensor_degree:
              print("\nWaring message using 3g phone to administrator")
              break
        else:
            continue
else:
    print("module not imported before")
