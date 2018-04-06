import sqlite3

conn = sqlite3.connect("contacts.sqlite")

name = input("Please enter your name : ")
sql_query = "SELECT * FROM contacts WHERE name LIKE ?"
for row in conn.execute(sql_query, (name,)):
    print(row)

conn.close()
