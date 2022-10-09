import sqlite3

conn = sqlite3.connect('student_database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE users (name TEXT, email TEXT, city TEXT, pincode TEXT)')
print("Table created successfully")
conn.close()