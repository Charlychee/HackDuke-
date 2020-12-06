import sqlite3
from models import User

conn = sqlite3.connect('bug.db')

c = conn.cursor()

def all_users():
    with sqlite3.connect("bug.db") as conn:
        c = conn.cursor()
        c.execute("SELECT name FROM users")
        newlist = []
        for i in c.fetchall():
            newlist.append(i[0])
        return newlist

def insert_user(netid, name, isAdmin, submissions, reward, types):
    with sqlite3.connect("bug.db") as conn:
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (:name, :isAdmin, :submissions, :reward, :types)", {'netid': netid, 'name': name, 'isAdmin': isAdmin, 'submissions' : submissions, 'reward' : reward, 'types' : types})
