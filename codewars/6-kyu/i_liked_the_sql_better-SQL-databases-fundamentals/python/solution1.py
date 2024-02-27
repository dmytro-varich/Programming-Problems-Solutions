# import library
import sqlite3
from sqlite3 import Error

conn = None 
db_file = r"/tmp/movies.db"

# Create a database /tmp/movies.db using SQLite3
try:
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    
    # Create a table in it called "MOVIES"
    cur.execute("""CREATE TABLE IF NOT EXISTS MOVIES (
        Name TEXT,
        Year INTEGER, 
        Rating INTEGER
    )""")
    
    # Insert data    
    cur.execute("INSERT INTO MOVIES VALUES ('Rise of the Planet of the Apes', 2011, 77)")
    cur.execute("INSERT INTO MOVIES VALUES ('Dawn of the Planet of the Apes', 2014, 91)")
    cur.execute("INSERT INTO MOVIES VALUES ('Alien', 1979, 97)")
    cur.execute("INSERT INTO MOVIES VALUES ('Aliens', 1986, 98)")
    cur.execute("INSERT INTO MOVIES VALUES ('Mad Max', 1979, 95)")
    cur.execute("INSERT INTO MOVIES VALUES ('Mad Max 2: The Road Warrior', 1981, 100)")
    conn.commit()
except Error as e:
    print(e)
finally:
    if conn:
        conn.close()
