#filename:file_stat_current_date.py(in chap 10)
#function: file modified time 

import os
import time
stat_info=[]

filename = 'd:\\book\\chap10\\sys_module.py'
stat_info = os.stat(filename)
print( '\n%s file''s Modified time is %s:'%(filename,time.ctime(stat_info.st_mtime)))
Mod_time=stat_info.st_mtime
print ("Modification time:",Mod_time)

#import time
import datetime
now_time=time.time()
print ("Current Date time is: %s" %time.time())

if Mod_time> now_time:
    print("the new file for test")
else:
    print("not new modified file")

