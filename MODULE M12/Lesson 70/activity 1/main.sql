CREATE TABLE NobelPrize (
    ID INT PRIMARY KEY,
    Year INT,
    Category VARCHAR(50),
    Winner VARCHAR(100),
    Country VARCHAR(50)
);

INSERT INTO NobelPrize VALUES (1, 2023, 'Physics', 'Pierre Agostini', 'USA');
INSERT INTO NobelPrize VALUES (2, 2023, 'Chemistry', 'Moungi Bawendi', 'USA');
INSERT INTO NobelPrize VALUES (3, 2023, 'Peace', 'Narges Mohammadi', 'Iran');
INSERT INTO NobelPrize VALUES (4, 2022, 'Physics', 'Alain Aspect', 'France');
INSERT INTO NobelPrize VALUES (5, 2022, 'Chemistry', 'Carolyn Bertozzi', 'USA');
INSERT INTO NobelPrize VALUES (6, 2021, 'Peace', 'Maria Ressa', 'Philippines');
INSERT INTO NobelPrize VALUES (7, 2021, 'Physics', 'Syukuro Manabe', 'USA');
INSERT INTO NobelPrize VALUES (8, 2020, 'Chemistry', 'Emmanuelle Charpentier', 'France');

SELECT * FROM NobelPrize ORDER BY Year DESC;

SELECT Category, COUNT(*) AS Winners FROM NobelPrize GROUP BY Category;

SELECT Country, COUNT(*) AS TotalWins
FROM NobelPrize
GROUP BY Country
HAVING COUNT(*) > 1
ORDER BY TotalWins DESC;

SELECT * FROM NobelPrize WHERE Category = 'Physics' ORDER BY Year DESC;
