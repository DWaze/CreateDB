import sqlite3

db = sqlite3.connect("contacts.sqlite")

query="SELECT * FROM contacts"

cursor = db.cursor()
cursor.execute(query)

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-"*20)

