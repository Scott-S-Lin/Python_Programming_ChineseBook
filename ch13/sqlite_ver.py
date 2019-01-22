#filename:sqlite_ver.py
#function: to check the sqlite version

import sqlite3 
import sys

con = None
dbfile="D:/BOOK/CHAP14/CHAP13_CUST.DB"

try:
    con = sqlite3.connect('dbfile.db')
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    ver = cur.fetchone()
    
    print ("SQLite3 version is as follows: %s" % ver)                
    
except sqlite3.Error as e:
   
    print ("Error %s:" % e.args[0])
    sys.exit(1)

else:
     print ("SQLite3 version is as follows: %s" % ver)

finally:
    if con:
        con.close()
