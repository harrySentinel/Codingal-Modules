import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

print("Using Aliases:")
cursor.execute("""
    SELECT e.Name AS EmployeeName, d.DeptName AS Department, e.Salary AS MonthlySalary
    FROM Employee e
    INNER JOIN Department d ON e.DeptID = d.DeptID
""")
for row in cursor.fetchall():
    print(row)

print("\nAlias on calculated column:")
cursor.execute("""
    SELECT Name, Salary, Salary * 12 AS AnnualSalary
    FROM Employee
    WHERE DeptID IS NOT NULL
""")
for row in cursor.fetchall():
    print(row)

conn.close()
