# filename:countdown_mp.py(chap11)
# function: multiprocessing
# Example of launching a process with the multiprocessing module

import time
import multiprocessing
#from multiprocessing import Process, Lock
import os

#inheirt from parent class multiprocessing.Process
class CountProcess(multiprocessing.Process):
    def __init__(self,count):
        print("--init--",count)
        multiprocessing. Process.__init__(self)
        self.count = count
        print('module name:', __name__)
        print('parent process:', os.getppid())
        print('process id:', os.getpid())
    def run(self):
        while self.count > 0:
            print ("Counting down", self.count)
            self.count -= 1
            time.sleep(5)
#        return

proclock = multiprocessing.Lock()

if __name__ == '__main__':

   proc1 = CountProcess(10)  # Create the process object
   proc1.start()             # Launch the process
   proc1.join()

   proc2 = CountProcess(20)  # Create another process
   proc2.start()                  # Launch
   proc2.join()
   
