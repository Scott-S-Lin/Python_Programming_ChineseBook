#filename:thread_fun.py
#function:thread using function

import threading
import time
sleep_sec=1
id=[]
def thrd_fun():
    print("\n now is doing the thread using function")
    for i in range(1, 3):
        time.sleep(sleep_sec)
        print("i=",i)
#    exit()
    
thrdobj=threading.Thread(target=thrd_fun)
thrdobj.start()
print(threading.active_count())
