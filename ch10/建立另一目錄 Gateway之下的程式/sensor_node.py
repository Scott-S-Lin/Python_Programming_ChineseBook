#filename:sensor_node.py
#function: the program in the package diretcory


class sensors:
    def __init__(self):
        '''sensor node constructor'''
        # Create the deafult sensor node id
        self.sensors_id = ['10001', '10002', '10003']
  
    def printnode(self):
        print("sensor id in the NY center park")
        print("-------------")
        for sensorid in self.sensors_id:
            print("\t%s " %sensorid)

test=sensors()
test.printnode()
