#filename:thrd_sync_timeout.py
#function: sync the thread using acuire and release

#(1)class threading.Lock
#   A simple mutual exclusion lock used to limit access to one thread.
#   This is a semaphore with s = 1.
#(2)acquire()
#   Obtain a lock. The process is blocked until the lock is available.
#(3)release()
#   Release the lock, and then if another thread is waiting for the lock, wake up that thread.
#(4)join(timeout=None)
#   Wait until the thread terminates.
#(5)acquire(blocking=True, timeout=-1)
#   Acquire a lock, blocking or non-blocking.
#   When invoked with the blocking argument set to True (the default),
#   block until the lock is unlocked, then set it to locked and return True.
#(6)timeout:When invoked with the floating-point timeout argument set to a positive value,
#   block for at most the number of seconds specified by timeout 
#   acquire(),The return value is True if the lock is acquired successfully,
#   False if not (for example if the timeout expired).
#(7)release()
#   Release a lock. This can be called from any thread, not only the thread which has acquired the lock.
#(8)join(timeout=None)
#   Wait until the thread terminates

import threading
import time
SLEEP=3
thrdid=[1,2]
loop_count=3
threads = []

class classThread (threading.Thread):
    def __init__(self, ID, name, counter):
        threading.Thread.__init__(self)
        self.ID = ID
        self.name = name
        self.counter = counter
    def run(self):
        print ("\n\nStarting thread " + self.name)
        
      
#        if(thrdLock.acquire(timeout=5)):
#            print("\nAcquire successful")
#            print ("\nacquired time is %s: %s\n" % (self.name, time.ctime(time.time())))
#        else:
#            print("\n timeout expired\n")
#            print ("\nacquired time is %s: %s\n" % (self.name, time.ctime(time.time())))
        
        if(thrdLock.acquire()): 
            print("\nAcquire successful")

        disp_time_used(self.name, self.counter, loop_count)

        # try to release the lock
        try:
            thrdLock.release()
        except RuntimeError:
            print("\nruntime error for ",self.name)

def disp_time_used(threadName, delay, count):
    while count:
        print("\n Thread id =",threading.get_ident()," Name=%s %s" % (threadName, time.ctime(time.time())))
        time.sleep(delay)
        count -= 1

thrdLock = threading.Lock()
#threads = []

# creat thread
thrd1 = classThread(thrdid[0], "Thread-1", SLEEP)
thrd2 = classThread(thrdid[1], "Thread-2", SLEEP)

# start the thread, it will call run()
print("THread Starting")
thrd1.start()
thrd2.start()

# add the thread to thread list
threads.append(thrd1)
threads.append(thrd2)

# Wait until the thread terminates
for t in threads:
    print("\n waiting for all thread terminates")
    t.join()
print ("Exit normally")
