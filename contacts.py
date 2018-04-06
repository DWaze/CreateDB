import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO CONTACTS(name, phone, email) VALUES('Tim',6545678,'tim@mail.com') ")
db.execute("INSERT INTO CONTACTS VALUES ('Brian', 1234,'brian@mymail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-"*20)

cursor.close()
db.commit()
db.close()
