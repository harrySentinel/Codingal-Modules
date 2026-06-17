import sqlite3

conn = sqlite3.connect("codingal.db")
print("Connected to SQLite database successfully!")

cursor = conn.cursor()
print("Cursor created.")

conn.close()
print("Connection closed.")
