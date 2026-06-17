import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("UPDATE Student SET Grade = 'A' WHERE Name = 'Neha Verma'")
conn.commit()
print("Record updated.")

cursor.execute("SELECT * FROM Student WHERE Name = 'Neha Verma'")
print("After update:", cursor.fetchone())

cursor.execute("DELETE FROM Student WHERE StudentID = 3")
conn.commit()
print("Record deleted.")

cursor.execute("SELECT * FROM Student")
print("\nFinal Table:")
for row in cursor.fetchall():
    print(row)

conn.close()
