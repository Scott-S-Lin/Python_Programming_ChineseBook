#fielname: dbformat.py
#function: sqlite3 insert data and commit using the format style
import sqlite3
import os

sqlite_file = "D:/BOOK/CHAP14/CHAP13_CUST.DB"
table_name = 'customers'
id_column = 'id'
name_column = 'cust_name'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

#c.execute("DROP TABLE IF EXISTS customers")
#c.execute("CREATE TABLE customers (Id INTEGER PRIMARY KEY , cust_name TEXT)")

# Inserts customer ID 
try:
    c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (1101, 'APPLE')".\
        format(tn=table_name, idf=id_column, cn=name_column))
    conn.commit()
except sqlite3.IntegrityError:
    print('**** ID exists ERROR  since it is PRIMARY KEY  {}'.format(id_column))
#    sys.exit(1)
#    if conn:
#        conn.rollback()
#    print ("Error %s:" % err.args[0])
#    sys.exit(1)
    

else:
    print("Sucessful")
    for row_record in c.execute("SELECT * FROM customers"):
        print (row_record)
    
# insert an customer ID if the ID not exist

c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (1102, 'APPLE')".\
        format(tn=table_name, idf=id_column, cn=name_column))

# Updates the  inserted or existing row record's cust_name         
c.execute("UPDATE {tn} SET {cn}=('IBM') WHERE {idf}=(1101)".\
        format(tn=table_name, cn=name_column, idf=id_column))

conn.commit()
print ("\nList all the records in the table after INSERT and Update :\n")
for row_record in c.execute("SELECT * FROM customers"):
    print (row_record)

conn.close()
