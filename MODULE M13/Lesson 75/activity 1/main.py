import sqlite3

conn = sqlite3.connect("store.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Product (
        ProductID INTEGER PRIMARY KEY,
        Name TEXT,
        Price REAL,
        Stock INTEGER
    )
""")

products = [
    (1, 'Laptop', 55000.0, 10),
    (2, 'Phone', 18000.0, 25),
    (3, 'Headphones', 2500.0, 40),
    (4, 'Tablet', 30000.0, 15)
]
cursor.executemany("INSERT INTO Product VALUES (?, ?, ?, ?)", products)
conn.commit()

print("All Products:")
cursor.execute("SELECT * FROM Product")
for row in cursor.fetchall():
    print(row)

print("\nProducts with Price > 20000:")
cursor.execute("SELECT * FROM Product WHERE Price > 20000")
for row in cursor.fetchall():
    print(row)

print("\nProducts sorted by Price:")
cursor.execute("SELECT * FROM Product ORDER BY Price DESC")
for row in cursor.fetchall():
    print(row)

cursor.execute("UPDATE Product SET Stock = Stock - 1 WHERE Name = 'Laptop'")
conn.commit()
print("\nStock updated for Laptop.")

cursor.execute("SELECT Name, Stock FROM Product WHERE Name = 'Laptop'")
print(cursor.fetchone())

conn.close()
