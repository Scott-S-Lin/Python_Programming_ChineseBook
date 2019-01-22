#filename:sub.py
#function: MQTT protocol for gateway and cloud computing

import sys
def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

try:
    import paho.mqtt.client as mqtt
    print("Names the module defines are:\n",dir(mqtt))
    print("use MQTT")
    mqttclt = mqtt.Client()
    mqttclt.on_message = on_message
    sys.exit()
except ImportError:
    print("Can not import")
    




