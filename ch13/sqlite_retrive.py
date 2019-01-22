#filename:Sqlite_retrive.py
#function: retrive row data
#The original table is created by using the following statement
#curr.execute("CREATE TABLE invest(date text, trans text, Company text, qty int, price real)")

import sqlite3 as DB
import sys


connDB = DB.connect('chap13_db.db')
with connDB:    
    cur = connDB.cursor()    
    cur.execute("SELECT * FROM invest")

    rows = cur.fetchall()
    print("The Data from invest table are as follows:\n")
    print(" date          trans  Company    qty  price")
    print("===========================================")
    for row in rows:
        print(row)

    cur.execute("SELECT * FROM invest WHERE Company= 'TSMC'  AND trans= 'BUY' ")

    BUY_amount=0
    amount=0
    BUY_records = cur.fetchall()
    print("\nThe Data from invest for TSMC BUY are as follows:\n")
    for row in BUY_records:
        print(row)
#   cur.execute("SELECT sum(qty*price) AS 'Total monthly salary' FROM invest")
        amount=row[3]*row[4]
        print("row amount=",amount)
        BUY_amount +=amount
    print("BUY_amount=",BUY_amount)

    cur.execute("SELECT * FROM invest WHERE Company= 'TSMC'  AND trans= 'SELL' ")

    SELL_amount=0
    amount=0
    SELL_records = cur.fetchall()
    print("\nThe Data from invest for TSMC SELL  are as follows:\n")
    for row in SELL_records:
        print(row)
        amount=row[3]*row[4]
        print("row amount=",amount) 
        SELL_amount +=amount
    print("SELL_amount=",SELL_amount)

    print(" The invest result=",(SELL_amount-BUY_amount)*1000," NTD")

# close the connection .
cur.close()
connDB.close()
