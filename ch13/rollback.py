#fielname: rollback.py
#function: rollback after commit
#          it will not rollback if no commit
import sqlite3
import os

sqlite_file = "D:/BOOK/CHAP14/CUST.DB"
table_name = 'customers'
id_column = 'id'
name_column = 'cust_name'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS customers")
c.execute("CREATE TABLE customers (Id INTEGER PRIMARY KEY , cust_name TEXT,dating TEXT, credit INTEGER NOT NULL)")

# Inserts customer ID 
try:

#   c.execute("BEGIN")
    customers_data = [(1170,'APPLE', '12/8/2000', 120000),
                     (1172,'IBM', '12/12/2005', 240000)]
    c.executemany("INSERT INTO customers VALUES (?,?,?,?)", customers_data)
#   c.commit()

except:
    c.execute("ROLLBACK")
    print("error ROLLBACK")
else:
    print("OK")
    

print ("\nList all the records in the table after INSERT and Update :\n")
for row_record in c.execute("SELECT * FROM customers"):
    print (row_record)

c.execute("ROLLBACK")
print ("\nList all the records in the table after INSERT and Update :\n")
for row_record in c.execute("SELECT * FROM customers"):
    print (row_record)

conn.close()
