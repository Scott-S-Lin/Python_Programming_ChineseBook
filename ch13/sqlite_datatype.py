#filename:sqlite_Datatype.py
#function: show the data type

import sqlite3
sql_create_cusomer_table = """
CREATE TABLE IF NOT EXISTS customer (
  Customer_id  INT  PRIMARY KEY  DEFAULT 1101,
  Cust_Name VARCHAR(10) NOT NULL DEFAULT "APPLE",
  Credit int  NOT NULL DEFAULT 10000,
  Phone   VARCHAR(10) NULL
);
"""

db_file ="D:/BOOK/CHAP14/CHAP13_TEST.DB" 

try:
        conn = sqlite3.connect(db_file)
        print(conn)
    
except Error as err:
        print(err)
else:
      print("OK")

conn.execute(sql_create_cusomer_table)

customer_data = [(1102,"APPLE",10000,"212-3312456"),
                 (1101,"IBM",20000,""),
                 (1103,"Google",30000,"716-3222222")]
cursor = conn.cursor()
cursor.executemany("INSERT INTO customer VALUES (?,?,?,?)", customer_data)
print ("\nList all the records in the table after INSERT :\n")
for row_record in cursor.execute("SELECT rowid, * FROM customer ORDER BY Customer_id"):
    print (row_record)
