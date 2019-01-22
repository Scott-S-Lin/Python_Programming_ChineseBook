#filename:module_sensor.py
#function: import fun_for_senor as s_node for convinence
#usage: if you want to use the module function or module variable
#the formt is : modulename.functionname
#               modulename.variable

import fun_for_sensor as s_node
degree=[]
node={}

s_node.sensor()
print ("now the data is from node id:",s_node.node_id)
degree.append(s_node.sensor_degree)

try:
    node[s_node.node_id]="TPE x=100 y=200"
except:
    print("error")

print("\nnode dict includes Nodeid and location=",node)
print("the current degree=",degree)
