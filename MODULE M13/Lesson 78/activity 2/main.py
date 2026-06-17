import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

print("Employees earning above average salary:")
cursor.execute("""
    SELECT Name, Salary
    FROM Employee
    WHERE Salary > (SELECT AVG(Salary) FROM Employee)
""")
for row in cursor.fetchall():
    print(row)

print("\nHighest paid employee in each department:")
cursor.execute("""
    SELECT Name, DeptID, Salary
    FROM Employee
    WHERE Salary IN (
        SELECT MAX(Salary) FROM Employee WHERE DeptID IS NOT NULL GROUP BY DeptID
    )
""")
for row in cursor.fetchall():
    print(row)

print("\nDepartments that have more than 1 employee:")
cursor.execute("""
    SELECT DeptName FROM Department
    WHERE DeptID IN (
        SELECT DeptID FROM Employee GROUP BY DeptID HAVING COUNT(*) > 1
    )
""")
for row in cursor.fetchall():
    print(row)

conn.close()
