import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Department (
        DeptID INTEGER PRIMARY KEY,
        DeptName TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
        EmpID INTEGER PRIMARY KEY,
        Name TEXT,
        DeptID INTEGER,
        Salary REAL,
        FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
    )
""")

cursor.executemany("INSERT INTO Department VALUES (?, ?)", [
    (1, 'Engineering'),
    (2, 'Marketing'),
    (3, 'HR')
])

cursor.executemany("INSERT INTO Employee VALUES (?, ?, ?, ?)", [
    (1, 'Aditya Srivastava', 1, 95000),
    (2, 'Riya Sharma', 2, 72000),
    (3, 'Aman Gupta', 1, 88000),
    (4, 'Neha Verma', 3, 65000),
    (5, 'Rohan Mehta', None, 50000)
])
conn.commit()

print("INNER JOIN - Employees with their Department:")
cursor.execute("""
    SELECT e.Name, d.DeptName, e.Salary
    FROM Employee e
    INNER JOIN Department d ON e.DeptID = d.DeptID
""")
for row in cursor.fetchall():
    print(row)

print("\nLEFT JOIN - All Employees including those without a Department:")
cursor.execute("""
    SELECT e.Name, d.DeptName, e.Salary
    FROM Employee e
    LEFT JOIN Department d ON e.DeptID = d.DeptID
""")
for row in cursor.fetchall():
    print(row)

conn.close()
