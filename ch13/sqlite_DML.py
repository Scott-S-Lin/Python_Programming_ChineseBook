#filename:sqlite_DML.py
#function: select Row data

import sqlite3 as DBlite

conn = DBlite.connect("D:/BOOK/CHAP14/CHAP13_TEST.DB") 
cursor = conn.cursor()
cursor.execute("""DROP TABLE if exists books""")

cursor.execute("""CREATE TABLE books
                  (book_id  text, title text, author text, release_date text, 
                   book_company text, category_type text) 
               """)
# insert data
cursor.execute("INSERT INTO books VALUES ('0-13-020272-x','Unix Network programming', 'Steven ', '10/12/2000', 'Osliiy', 'Network')")
# save data to database
conn.commit()

# insert multiple records(row) using cursorname.execitemany 
BOOKS_data = [('1-878739-02-6','c++ primer', 'Stephen', '12/8/2000', 'Waite Group', 'Language'),
              ('0-13-2017-1','The design of the UNix OS','J.Bach', '3/2/2002', 'Prentice', 'OS'),
              ('0-13-2016-1','The Python programming','S.HSU', '3/2/2016', 'songkung', 'language')]
cursor.executemany("INSERT INTO books VALUES (?,?,?,?,?,?)", BOOKS_data)
conn.commit()

print ("\nList all the records in the table after INSERT :\n")
for row_record in cursor.execute("SELECT rowid, * FROM books ORDER BY category_type"):
    print (row_record)
    
print( "\nResults from a LIKE query:\n")
select_sql = """
SELECT * FROM books 
WHERE title LIKE '%python%' """
cursor.execute(select_sql)
print (cursor.fetchall())

print( "\nDELETE author is J.Bach:\n")
delete_sql="""DELETE FROM  books where author="J.Bach"
"""
cursor.execute(delete_sql)
conn.commit()
for row_record in cursor.execute("SELECT rowid, * FROM books ORDER BY category_type"):
    print (row_record)






