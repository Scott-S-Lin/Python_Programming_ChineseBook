#filename: App_cars.py
#function: use the SQLite in the application for car database

import sqlite3 as lite
import sys
dbfile="D:/BOOK/CHAP14/CUST.DB"

con = lite.connect(dbfile)
with con:
    
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("CREATE TABLE cars(Id INT PRIMARY KEY, Name TEXT, MODEL TEXT DEFAULT 'normal' ,year INT)")
    cur.execute("INSERT INTO cars VALUES(1100,'BMW', 'BMW X5',1965)")
    cur.execute("INSERT INTO cars VALUES(1101,'HYYDAI','NORMAL',1965)")

    cars_data = [(1105,'AUDI','A6', 1965),
                 (1102,'Mercedes','S3', 2001),
                 (1107,'TOYOTA','Camery',2010)
                ]
    cur.executemany("INSERT INTO cars VALUES (?,?,?,?)", cars_data)
   

print ("\nList all the records in the table after INSERT :\n")
for row_record in cur.execute("SELECT rowid, * FROM cars ORDER BY Name"):
    print (row_record)


print ("\nList all the records in the table after SELECT:\n")    
for row_record in cur.execute("SELECT * FROM cars WHERE Name = 'AUDI'"):
     print (row_record)

con.close()
