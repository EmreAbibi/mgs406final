import sqlite3

conn = sqlite3.connect('ferry.db')

print("Opened database successfully!")

conn.execute('CREATE TABLE reservations (ResName TEXT NOT NULL, ResDate DATE NOT NULL, ResTime TIME NOT NULL, ResParty INTEGER NOT NULL)')

print ("Table created successfully")

conn.close
