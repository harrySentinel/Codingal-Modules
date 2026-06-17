CREATE TABLE Salesman (
    SalesmanID INT PRIMARY KEY,
    Name VARCHAR(50),
    City VARCHAR(30),
    Commission DECIMAL(4, 2)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    Amount DECIMAL(10, 2),
    OrderDate DATE,
    CustomerID INT,
    SalesmanID INT,
    FOREIGN KEY (SalesmanID) REFERENCES Salesman(SalesmanID)
);

INSERT INTO Salesman VALUES (101, 'Aditya Srivastava', 'Mumbai', 0.15);
INSERT INTO Salesman VALUES (102, 'Riya Sharma', 'Delhi', 0.13);
INSERT INTO Salesman VALUES (103, 'Aman Gupta', 'Pune', 0.11);
INSERT INTO Salesman VALUES (104, 'Neha Verma', 'Chennai', 0.12);

INSERT INTO Orders VALUES (5001, 1500.00, '2024-01-10', 201, 101);
INSERT INTO Orders VALUES (5002, 2200.00, '2024-01-15', 202, 102);
INSERT INTO Orders VALUES (5003, 800.00,  '2024-01-20', 203, 101);
INSERT INTO Orders VALUES (5004, 3400.00, '2024-02-01', 204, 103);
INSERT INTO Orders VALUES (5005, 950.00,  '2024-02-10', 205, 104);

SELECT * FROM Salesman;
SELECT * FROM Orders;

SELECT s.Name, o.OrderID, o.Amount
FROM Salesman s
JOIN Orders o ON s.SalesmanID = o.SalesmanID;
