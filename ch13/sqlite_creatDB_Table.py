#filename:sqlite_CreateDB_Table.py
#function: Python program using Sqlite
#Step1: Create user DB name using Sqlite3.connect("DB name)
#step2: Create Table using CREATE TABLE Table_name
#step3: insert Data value using INSERT INTO invest VALUES

import sqlite3
conndb = sqlite3.connect('chap13_DB.db')
curr = conndb.cursor()

# Create table using CREATE TABLE Table_name
curr.execute("CREATE TABLE invest(date text, trans text, Company text, qty int, price real)")

# Insert a row of data
curr.execute("INSERT INTO invest VALUES ('2016-03-01','BUY','Mediatek',10,120)")

# commit the changes, it means save the data
conndb.commit()

curr.execute('select * from invest')
data_fromDB=curr.fetchall()
print(data_fromDB)

# inserts many records at a time
buy_sell = [('2016-03-28', 'BUY', 'Mediatek', 10, 123.00),
             ('2016-05-02', 'BUY', 'TSMC', 20, 120.00),
             ('2006-05-12', 'SELL','Mediatek', 10, 125.00),
             ('2006-05-13', 'SELL','TSMC', 20, 125.00),
            ]
curr.executemany('INSERT INTO invest VALUES (?,?,?,?,?)', buy_sell)
conndb.commit()

#fetch the data from DB's table
curr.execute('select * from invest')
data=curr.fetchall()
print(data)

# close the connection .
curr.close()
conndb.close()

