import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('test.db')

cur = conn.cursor()

# create user table
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("create table if not exists users (id INTEGER PRIMARY KEY, username TEXT, email TEXT, password TEXT)")

# add users to table
cur.execute("insert into users (username, email, password) values (?, ?, ?)", ("bschippe", "bschippe@nd.edu", "Yum"))
cur.execute("insert into users (username, email, password) values (?, ?, ?)", ("jsteve22", "jsteve22@nd.edu", "jsteve22"))

cur.execute("select * from users")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()