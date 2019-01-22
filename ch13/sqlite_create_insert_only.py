#filename:sqlite_Create_insert_only.py
#function: create Database name and Table and insrt values

import sqlite3 as DBlite

conn = DBlite.connect("D:/BOOK/CHAP14/CHAP13_TEST.DB") 
cursor = conn.cursor()

cursor.execute("""drop table if exists books""")

# create a table
#cursor.execute("""CREATE TABLE albums
#                  (title text, artist text, release_date text, 
#                   publisher text, media_type text) 
#               """)
cursor.execute("""CREATE TABLE books
                  (book_id  text, title text, author text, release_date text, 
                   book_company text, category_type text) 
               """)
# insert some data
cursor.execute("INSERT INTO books VALUES ('0-13-020272-x','Unix Network programming', 'Steven ', '10/12/2000', 'Osliiy', 'Network')")

# commit, means to save data to database
conn.commit()

# insert multiple records, using the more secure "?" method
#cursorname.execitemany
BOOKS_data = [('1-878739-02-6','c++ primer', 'Stephen', '12/8/2000', 'Waite Group', 'Language'),
              ('0-13-2017-1','The design of the UNix OS','J.Bach', '3/2/2002', 'Prentice', 'OS')]
cursor.executemany("INSERT INTO books VALUES (?,?,?,?,?,?)", BOOKS_data)
conn.commit()

print ("\nList all the records in the table after INSERT :\n")
for row_record in cursor.execute("SELECT rowid, * FROM books ORDER BY category_type"):
    print (row_record)

embedded_sql_alter = """
ALTER TABLE books ADD price int
"""
cursor.execute(embedded_sql_alter)
conn.commit()

print ("\nList all the records in the table after ALTER :\n")
for row_record in cursor.execute("SELECT rowid, * FROM books ORDER BY category_type"):
    print (row_record)

embedded_sql = """
UPDATE books SET author = 'Maurice J.Bach' WHERE author = 'J.Bach'
"""
cursor.execute(embedded_sql)
conn.commit()
print ("\nList all the records in the table after UPDATE :\n")
for row_record in cursor.execute("SELECT rowid, * FROM books ORDER BY category_type"):
    print (row_record)


sql = """ DELETE FROM books WHERE author = 'Stephen'
"""
cursor.execute(sql)
conn.commit()
print ("\nList all the records in the table after DELETE FROM TABLE:\n")
for row_record in cursor.execute("SELECT rowid, * FROM books ORDER BY category_type"):
    print (row_record)




