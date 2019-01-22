
#filename:employee_count.py
#function: create database and create table, insert value to table

import sqlite3
dbfile= "D:/BOOK/CHAP13/employee.DB"
connection = sqlite3.connect(dbfile)

cursor = connection.cursor()

# delete the table first
cursor.execute("""DROP TABLE employee;""")

sql_CREATE_TABLE = """
CREATE TABLE employee ( 
emp_id INTEGER PRIMARY KEY, first VARCHAR(10), last VARCHAR(8), 
sex CHAR(1), hire DATE,birth DATE,salary int);
"""

cursor.execute(sql_CREATE_TABLE)

sql_INSERT = """INSERT INTO employee (emp_id, first, last, sex, hire,birth,salary)
    VALUES (1999, "Steven", "Bush", "M","2000-01-26", "1966-12-25",5000);"""
cursor.execute(sql_INSERT)

sql_INSERT = """INSERT INTO employee (emp_id, first, last, sex, hire,birth,salary)
    VALUES (1990, "John", "Hu", "M","2006-05-26", "1990-1-25",5500);"""
cursor.execute(sql_INSERT)

sql_INSERT_command = """INSERT INTO employee (emp_id, first, last, sex, hire,birth,salary)
    VALUES (2000, "Ted", "HSU", "M","1980-01-26", "1963-10-25",4000);"""
cursor.execute(sql_INSERT_command)


# use commit() when you want to save the changes
connection.commit()
cursor.execute("SELECT COUNT(*) from employee where salary >4000 AND first='John'")
(number_of_rows,)=cursor.fetchone()
print("count=",number_of_rows)
 

connection.close()
