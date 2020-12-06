import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")
try:
    conn.execute('CREATE TABLE users (name TEXT)')
except:
    print("nope")

def removeUser(name):
    with sqlite3.connect("database.db") as conn:
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE name = :name",{'name' : name})



conn.close()