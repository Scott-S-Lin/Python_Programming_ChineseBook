# filename:perform_mp.py
# funcion: performance test comparison between sequential and multiprocessing
# 

import time
import multiprocessing

def count(n):
    
    while n > 0:
        n -= 1

starting = time.time()
print ("\nstarting time %s: " %time.ctime(time.time()))
count(5000000)
count(5000000)
ending = time.time()
print ("ending time   %s: " %time.ctime(time.time()))
print ("Sequential process performance     :", ending-starting)

start = time.time()
print ("\nstarting time %s: " %time.ctime(time.time()))
p1 = multiprocessing.Process(target=count,args=(5000000,))
p2 = multiprocessing.Process(target=count,args=(5000000,))
p1.start()
p2.start()
p1.join()
p2.join()
end = time.time()
print ("ending time   %s: " %time.ctime(time.time()))
print ("Multiprocessing process performance:", end-start)

