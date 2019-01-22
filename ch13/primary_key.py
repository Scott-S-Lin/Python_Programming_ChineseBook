#filename: primary_key.py
#function: create table using primay key and select two table such as orders and customers

import sqlite3


#create a Database
def db_connect(db):
   
    try:
        conn = sqlite3.connect(db)
        print("conn=",conn)
        return conn
    except Error as err:
        print(err)
        return None
    else:
        print("connection DB is ok")
        
def create_table(conn, create_table):
    try:
        c = conn.cursor()
        c.execute(create_table)
    except Error as err:
        print(err)
        return NONE
    else:
        print("Create TABLE OK")
        return c
    finally:
        print("Finally")

def main():
    dbfile ="D:/BOOK/CHAP14/CHAP13_TEST.DB"
    
    sql_create_customers_table = """ CREATE TABLE IF NOT EXISTS customers (
                                        id         integer PRIMARY KEY,
                                        name       text NOT NULL,
                                        begin_date text,
                                        credit     integer NOT NULL
                                    ); """
 
    sql_create_orders_table = """CREATE TABLE IF NOT EXISTS orders (
                                    id            integer PRIMARY KEY,
                                    name          text NOT NULL,
                                    quantity      integer,
                                    product       integer NOT NULL,
                                    price         integer NOT NULL,
                                    ship_date     text NOT NULL,
                                    FOREIGN KEY   (id) REFERENCES customers (id)
                                );"""
 
    # create a database connection
    conn = db_connect(dbfile)
    
    if conn is not None:
        create_table(conn, sql_create_customers_table)
        create_table(conn, sql_create_orders_table)
    else:
        print("CANNOT  create the database connection.")

#    insert_values, don't let the primary key id duplicate , it is PRIMARY KEY 
    c = conn.cursor()
#    c.execute(" DROP TABLE customers")
    customers_data = [(1176,'APPLE', '12/8/2000', 120000),
                     (1178,'IBM', '12/12/2005', 240000)]
    c.executemany("INSERT INTO customers VALUES (?,?,?,?)", customers_data)
    conn.commit()
    print ("\nList all the records in the table after INSERT customers:\n")
    for row_record in c.execute("SELECT * FROM customers ORDER BY id"):
        print (row_record)
        
    c = conn.cursor()
#    c.execute(" DROP TABLE orders")
    orders_data = [(1176,'APPLE', 200, "AVL car L1", 100,'12/05/2016'),
                   (1178,'IBM', 300,"AVL car L2",150,'12/06/2015')]
    c.executemany("INSERT INTO orders VALUES (?,?,?,?,?,?)", orders_data)
    conn.commit()
    print ("\nList all the records in the table after INSERT orders:\n")
    for row_record in c.execute("SELECT * FROM orders ORDER BY id"):
        print (row_record)
    print ("\nList all the records in the table after SELECT:\n")    
    for row_record in c.execute("SELECT * FROM orders WHERE EXISTS(SELECT * FROM customers WHERE customers.id=orders.id)"):
        print (row_record)    
    
if __name__ == '__main__':
    main()
