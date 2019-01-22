#filenam:thrd_class.py
#function: thread using class
#class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
#name:the thread name
#name is constructed of the form “Thread-N” where N is a small decimal number

import threading
import time
import sys

thrdlist=[]
delay_sec=5
thread_thread_delay=.3  

class cls_Thread(threading.Thread):
    def run(self):
        print("{} is Active!!!".format(self.getName())) # "Thread-x" active
        print ("\n%s: %s" % (self.getName(), time.ctime(time.time())))
        time.sleep(delay_sec)                        # delay 
        print("\n{} is finish!".format(self.getName()))   # "Thread-x" finish
        print ("\n%s: %s" % (self.getName(), time.ctime(time.time())))

if __name__ == '__main__':
#    print("\n thread acive count=",threading.active_count())
    
    for i in range(2):
        thrd = cls_Thread(name = "Thread-{}".format(i + 1)) #give thread unique ID
        thrd.start() 
        time.sleep(thread_thread_delay) #wait 
    

   
