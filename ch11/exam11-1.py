# filename:chap12_ex2_count_down.py
# function: invoke target function to a different thread, and check the time

import time
import threading
count_val=10

def target_counting(count):
    while count > 0:
        count -= 1
        time.sleep(0.5)
    return

print ("\nstarting time %s: " %time.ctime(time.time()))
thrd1 = threading.Thread(target=target_counting,args=(count_val,))
thrd1.start()
#thrd1.join()
print ("\nstarting time %s: " %time.ctime(time.time()))
thrd2 = threading.Thread(target=target_counting,args=(count_val*2,))
thrd2.start()
#thrd2.join()
print ("\nstarting time %s: " %time.ctime(time.time()))
