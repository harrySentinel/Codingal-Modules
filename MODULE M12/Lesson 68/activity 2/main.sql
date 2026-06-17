CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Category VARCHAR(30),
    Price DECIMAL(10, 2),
    Stock INT
);

INSERT INTO Product VALUES (1, 'Laptop', 'Electronics', 55000.00, 30);
INSERT INTO Product VALUES (2, 'Phone', 'Electronics', 18000.00, 100);
INSERT INTO Product VALUES (3, 'Notebook', 'Stationery', 50.00, 500);
INSERT INTO Product VALUES (4, 'Headphones', 'Electronics', 2500.00, 75);
INSERT INTO Product VALUES (5, 'Pen', 'Stationery', 20.00, 1000);
INSERT INTO Product VALUES (6, 'Tablet', 'Electronics', 30000.00, 50);

SELECT * FROM Product WHERE Price > 10000;

SELECT * FROM Product WHERE Category = 'Electronics' AND Price < 25000;

SELECT * FROM Product WHERE Price BETWEEN 1000 AND 30000;

SELECT * FROM Product WHERE ProductName LIKE '%e%';

SELECT * FROM Product ORDER BY Price ASC;

SELECT * FROM Product WHERE Stock > 50 AND Category = 'Electronics';
