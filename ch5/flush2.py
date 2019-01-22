#filename:flush2.py
#function: it shows that stdout has a buffering
#sys.stdout.flush() will flush the Stdout buffer, it is better for use
#sys.stdout.flush() it will clear the stdout buffer, so the str(count) data will be showed each time , not until all process complete
#import time needed, it used for time.sleep(..)
#import datetime is needed, it is used for datetime.datetime.now()

import time 
import sys 
import datetime

nowtime = datetime.datetime.now()
print ("\nCurrent minute second: %d : %d" % (nowtime.minute,nowtime.second))

for val in range(5): 
    sys.stdout.write("..writeData..")
    sys.stdout.write(str(val))
    sys.stdout.flush()
    time.sleep(1)
    
sys.stdout.write("\nloop Done!")
nowtime = datetime.datetime.now()
print ("\nCurrent minute second: %d : %d" % (nowtime.minute,nowtime.second))


