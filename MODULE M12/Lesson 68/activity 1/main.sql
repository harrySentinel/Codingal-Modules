CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Grade VARCHAR(5),
    Marks INT,
    City VARCHAR(30)
);

INSERT INTO Student VALUES (1, 'Aditya Srivastava', 20, 'A', 92, 'Mumbai');
INSERT INTO Student VALUES (2, 'Riya Sharma', 19, 'B', 78, 'Delhi');
INSERT INTO Student VALUES (3, 'Aman Gupta', 21, 'A', 88, 'Pune');
INSERT INTO Student VALUES (4, 'Neha Verma', 20, 'C', 65, 'Mumbai');
INSERT INTO Student VALUES (5, 'Rohan Mehta', 22, 'B', 74, 'Chennai');
INSERT INTO Student VALUES (6, 'Priya Singh', 19, 'A', 95, 'Delhi');

SELECT * FROM Student WHERE Marks > 80;

SELECT * FROM Student WHERE City = 'Mumbai' AND Grade = 'A';

SELECT * FROM Student WHERE Marks BETWEEN 70 AND 90;

SELECT * FROM Student WHERE City IN ('Mumbai', 'Delhi');

SELECT * FROM Student WHERE Name LIKE 'A%';

SELECT * FROM Student ORDER BY Marks DESC;
