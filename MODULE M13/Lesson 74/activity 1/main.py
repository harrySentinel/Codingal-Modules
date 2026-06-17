import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Student (
        StudentID INTEGER PRIMARY KEY,
        Name TEXT,
        Age INTEGER,
        Grade TEXT
    )
""")

cursor.execute("INSERT INTO Student VALUES (1, 'Aditya Srivastava', 20, 'A')")
cursor.execute("INSERT INTO Student VALUES (2, 'Riya Sharma', 19, 'B')")
cursor.execute("INSERT INTO Student VALUES (3, 'Aman Gupta', 21, 'A')")
cursor.execute("INSERT INTO Student VALUES (4, 'Neha Verma', 20, 'C')")

conn.commit()

cursor.execute("SELECT * FROM Student")
rows = cursor.fetchall()

print("Student Table:")
for row in rows:
    print(row)

conn.close()
