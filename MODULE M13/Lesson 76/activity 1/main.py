import sqlite3

conn = sqlite3.connect("constraints.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
        EmpID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Email TEXT UNIQUE,
        Age INTEGER CHECK(Age >= 18),
        Salary REAL DEFAULT 30000.0
    )
""")

cursor.execute("INSERT INTO Employee (EmpID, Name, Email, Age) VALUES (1, 'Aditya Srivastava', 'aditya@codingal.com', 25)")
cursor.execute("INSERT INTO Employee (EmpID, Name, Email, Age, Salary) VALUES (2, 'Riya Sharma', 'riya@gmail.com', 22, 45000)")
cursor.execute("INSERT INTO Employee (EmpID, Name, Email, Age, Salary) VALUES (3, 'Aman Gupta', 'aman@gmail.com', 30, 60000)")
conn.commit()

cursor.execute("SELECT * FROM Employee")
print("Employee Table:")
for row in cursor.fetchall():
    print(row)

conn.close()
