#filenme:chap10_ex2_date.py
#funtion:Get cunrrent Date

import datetime
date_time = datetime.datetime.now()
 

print ("DD/MM/YY  =  %s/%s/%s" % (date_time.day, date_time.month, date_time.year) )
print ("hh:mm:ss = %s:%s:%s" % (date_time.hour, date_time.month, date_time.second) )


