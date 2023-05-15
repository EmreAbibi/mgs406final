import mysql.connector as sql

conn = sql.connect(host = 'localhost', user = 'flask', password = 'ubuntu')
cur = conn.cursor()

print(conn)

cmd = "CREATE DATABASE ferry"
cur.execute(cmd)

conn.close()

conn2 = sql.connect(host = 'localhost', user = 'flask', password = 'ubuntu', database = 'ferry')
cur2 = conn2.cursor()

table = 'CREATE TABLE reservations (ResName TEXT NOT NULL, ResDate DATE NOT NULL, ResTime TIME NOT NULL, ResParty INTEGER NOT NULL)'

cur2.execute(table)

conn2.close()
