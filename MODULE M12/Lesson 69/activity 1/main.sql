CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Category VARCHAR(30),
    Price DECIMAL(10, 2),
    Quantity INT
);

INSERT INTO Products VALUES (1, 'Laptop', 'Electronics', 55000.00, 10);
INSERT INTO Products VALUES (2, 'Phone', 'Electronics', 18000.00, 25);
INSERT INTO Products VALUES (3, 'Notebook', 'Stationery', 50.00, 200);
INSERT INTO Products VALUES (4, 'Headphones', 'Electronics', 2500.00, 40);
INSERT INTO Products VALUES (5, 'Pen', 'Stationery', 20.00, 500);
INSERT INTO Products VALUES (6, 'Tablet', 'Electronics', 30000.00, 15);
INSERT INTO Products VALUES (7, 'Eraser', 'Stationery', 10.00, 300);

SELECT COUNT(*) AS TotalProducts FROM Products;

SELECT SUM(Price) AS TotalPrice FROM Products;

SELECT AVG(Price) AS AveragePrice FROM Products;

SELECT MAX(Price) AS MostExpensive FROM Products;

SELECT MIN(Price) AS CheapestProduct FROM Products;

SELECT Category, COUNT(*) AS Count, AVG(Price) AS AvgPrice
FROM Products
GROUP BY Category;
