CREATE TABLE Department (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50),
    Location VARCHAR(30)
);

CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(50),
    DeptID INT,
    Salary DECIMAL(10, 2),
    JoinYear INT,
    FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
);

INSERT INTO Department VALUES (1, 'Engineering', 'Mumbai');
INSERT INTO Department VALUES (2, 'Marketing', 'Delhi');
INSERT INTO Department VALUES (3, 'HR', 'Bangalore');

INSERT INTO Employee VALUES (1, 'Aditya Srivastava', 1, 95000.00, 2020);
INSERT INTO Employee VALUES (2, 'Riya Sharma', 2, 72000.00, 2021);
INSERT INTO Employee VALUES (3, 'Aman Gupta', 1, 88000.00, 2019);
INSERT INTO Employee VALUES (4, 'Neha Verma', 3, 65000.00, 2022);
INSERT INTO Employee VALUES (5, 'Rohan Mehta', 2, 78000.00, 2020);
INSERT INTO Employee VALUES (6, 'Priya Singh', 1, 91000.00, 2021);

SELECT d.DeptName, COUNT(e.EmpID) AS TotalEmployees, AVG(e.Salary) AS AvgSalary
FROM Department d
JOIN Employee e ON d.DeptID = e.DeptID
GROUP BY d.DeptName
ORDER BY AvgSalary DESC;

SELECT d.DeptName, MAX(e.Salary) AS MaxSalary, MIN(e.Salary) AS MinSalary
FROM Department d
JOIN Employee e ON d.DeptID = e.DeptID
GROUP BY d.DeptName
HAVING AVG(e.Salary) > 70000;
