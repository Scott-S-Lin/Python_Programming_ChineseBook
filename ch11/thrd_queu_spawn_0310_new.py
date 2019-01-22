#filename:thrd_queu_spawn_0310_new.py
#function:thread using queue
 

import threading, queue
import working_data

queue_result=[]
THREAD_NO = 2                   # This is how many threads we want
jobs = queue.Queue(5)           # This sets up the queue object to use 5 slots
singlelock = threading.Lock()   # This is a lock so threads don't print trough each other (and other reasons)
Timeout=3


#This is called from the main function
#called: by main function
#input: the input data is from Working_data module

def thrdprocess(inputdata):  
#    print ("input data from module working_data is:",inputdata)
 
    # Spawn the threads
    print ("\nActivate {0} threads.".format(THREAD_NO))
    for x in range(THREAD_NO):
        print ("Thread {0} started.".format(x+1))
        # it will call run(),this  is the thread class that we instant
        worker().start()
 
    
#put the data in the queue    
    for i in inputdata:     
         try:
        # Block if queue is full, and wait 3 seconds. After 3 sec  raise Queue Full error.     
#            jobsqueue.put(i, block=True, timeout=Timeout)
            jobs.put(i, block=True, timeout=Timeout)    
         except:
            singlelock.acquire()
            print ("\nThe queue is full !")
            singlelock.release()
 
    # Wait for the threads to finish
    print ("Waiting for threads to finish.")
    jobs.join()                 # waits for all threads to finish.
    print("\n all finished")
    print(queue_result)


# This class is a thread template
# purpose:to spawn those threads.
# run function's purpose in the class:
# is to  gets a job out of the jobs queue, and then lets the queue object know when it has finished.


class worker(threading.Thread):
    def run(self):
        print("\n Working....\n")
        # run forever
        while 1:
            # Try and get a job out of the queue
            try:               
                queuedata = jobs.get(True,1)
                singlelock.acquire()        # Acquire the lock
                res=(queuedata[0]*queuedata[1])
                queue_result.append(res)
                singlelock.release()        # Release the lock
                # Let the queue know the job is finished.
                jobs.task_done()
            except:
                break           # No more jobs in the queue
           
if __name__ == '__main__':
    # Call the main function that sets up threading.
    thrdprocess(working_data.inputlist)
