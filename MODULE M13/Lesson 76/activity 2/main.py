import sqlite3

conn = sqlite3.connect("constraints.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables in database:")
for table in tables:
    print("-", table[0])

print("\nEmployee Table Info:")
cursor.execute("PRAGMA table_info(Employee)")
for col in cursor.fetchall():
    print(col)

try:
    cursor.execute("INSERT INTO Employee (EmpID, Name, Email, Age) VALUES (4, 'Neha', 'aditya@codingal.com', 20)")
    conn.commit()
except sqlite3.IntegrityError as e:
    print("\nConstraint Error:", e)

try:
    cursor.execute("INSERT INTO Employee (EmpID, Name, Email, Age) VALUES (5, 'Rohan', 'rohan@gmail.com', 15)")
    conn.commit()
except sqlite3.IntegrityError as e:
    print("Constraint Error:", e)

conn.close()
