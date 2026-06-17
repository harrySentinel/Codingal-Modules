CREATE TABLE Supplier (
    SupplierID INT PRIMARY KEY,
    SupplierName VARCHAR(50),
    City VARCHAR(30),
    Country VARCHAR(30),
    Phone VARCHAR(15)
);

INSERT INTO Supplier VALUES (1, 'Aditya Traders', 'Mumbai', 'India', '9876543210');
INSERT INTO Supplier VALUES (2, 'Riya Supplies', 'Delhi', 'India', '9123456780');
INSERT INTO Supplier VALUES (3, 'Aman Exports', 'Bangalore', 'India', '9988776655');
INSERT INTO Supplier VALUES (4, 'Global Goods', 'New York', 'USA', '1234567890');
INSERT INTO Supplier VALUES (5, 'Neha Imports', 'London', 'UK', '4412345678');

SELECT * FROM Supplier;

SELECT SupplierName, City FROM Supplier WHERE Country = 'India';
