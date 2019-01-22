#filename:chap13_ex1_create_table
#function:check why the sytax is wrong

import sqlite3

#-------------------------db creation ---------------------------------------#
dbconn = sqlite3.connect('/my_db.db')
cursor = dbconn.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
dbconn.execute('''CREATE TABLE EMPLOYEE
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')


cursor.execute("DROP TABLE IF EXISTS IOT_table")
sql = """CREATE TABLE IOT_table (
        name        TEXT DEFAULT NULL,
        temperature INT,
        location    CHAR(50),
        );"""
cursor.execute(sql)

sql = ("CREATE INDEX index_iot_table ON IOT_table(name);")
cursor.execute(sql)
