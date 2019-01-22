#filename:thrd_example.py
#function: using the threading 

import time
from threading import Thread
sec=2

def thrdsleep(id):
    print ("\nsleep %d sec by thread-id %d" % (sec,id))
    time.sleep(sec)
    print ("\nfinish sleep by thread-id %d" % id)

print("\n\n")
for i in range(3):
    thrd = Thread(target=thrdsleep, args=(i+1,))
    thrd.start()
