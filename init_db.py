import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute( """
CREATE TABLE students (
  id INTEGER PRIMARY KEY AUTOINCREMENT ,
  name TEXT NOT NULL ,
  email TEXT NOT NULL ,
  department TEXT NOT NULL
)
""" )

conn.commit ()
conn.close ()

print( " Database created successfully ! " )