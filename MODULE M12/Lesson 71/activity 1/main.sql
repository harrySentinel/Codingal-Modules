CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(50),
    Email VARCHAR(100),
    City VARCHAR(30),
    JoinDate DATE
);

CREATE TABLE Item (
    ItemID INT PRIMARY KEY,
    ItemName VARCHAR(50),
    Price DECIMAL(10, 2),
    Category VARCHAR(30)
);

CREATE TABLE Purchase (
    PurchaseID INT PRIMARY KEY,
    CustomerID INT,
    ItemID INT,
    Quantity INT,
    PurchaseDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (ItemID) REFERENCES Item(ItemID)
);

INSERT INTO Customer VALUES (1, 'Aditya Srivastava', 'aditya@codingal.com', 'Mumbai', '2023-01-15');
INSERT INTO Customer VALUES (2, 'Riya Sharma', 'riya@gmail.com', 'Delhi', '2023-03-10');
INSERT INTO Customer VALUES (3, 'Aman Gupta', 'aman@gmail.com', 'Pune', '2023-06-20');
INSERT INTO Customer VALUES (4, 'Neha Verma', 'neha@gmail.com', 'Chennai', '2024-01-05');

INSERT INTO Item VALUES (1, 'Laptop', 55000.00, 'Electronics');
INSERT INTO Item VALUES (2, 'Phone', 18000.00, 'Electronics');
INSERT INTO Item VALUES (3, 'Bag', 1200.00, 'Accessories');
INSERT INTO Item VALUES (4, 'Headphones', 2500.00, 'Electronics');

INSERT INTO Purchase VALUES (1, 1, 1, 1, '2024-01-20');
INSERT INTO Purchase VALUES (2, 2, 2, 2, '2024-02-10');
INSERT INTO Purchase VALUES (3, 1, 4, 1, '2024-02-15');
INSERT INTO Purchase VALUES (4, 3, 3, 3, '2024-03-01');
INSERT INTO Purchase VALUES (5, 4, 2, 1, '2024-03-10');

SELECT c.Name, i.ItemName, p.Quantity, (i.Price * p.Quantity) AS TotalAmount
FROM Customer c
JOIN Purchase p ON c.CustomerID = p.CustomerID
JOIN Item i ON p.ItemID = i.ItemID
ORDER BY TotalAmount DESC;

SELECT c.Name, SUM(i.Price * p.Quantity) AS TotalSpent
FROM Customer c
JOIN Purchase p ON c.CustomerID = p.CustomerID
JOIN Item i ON p.ItemID = i.ItemID
GROUP BY c.Name
ORDER BY TotalSpent DESC;

SELECT i.Category, SUM(p.Quantity) AS TotalSold
FROM Item i
JOIN Purchase p ON i.ItemID = p.ItemID
GROUP BY i.Category;
