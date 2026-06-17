CREATE TABLE Restaurant (
    RestaurantID INT PRIMARY KEY,
    Name VARCHAR(100),
    Cuisine VARCHAR(50),
    Borough VARCHAR(30),
    Rating DECIMAL(3, 1),
    PriceRange VARCHAR(10)
);

CREATE TABLE MenuItem (
    MenuID INT PRIMARY KEY,
    RestaurantID INT,
    Dish VARCHAR(100),
    Price DECIMAL(8, 2),
    Category VARCHAR(30),
    FOREIGN KEY (RestaurantID) REFERENCES Restaurant(RestaurantID)
);

INSERT INTO Restaurant VALUES (1, 'The Brooklyn Diner', 'American', 'Brooklyn', 4.5, '$$');
INSERT INTO Restaurant VALUES (2, 'Spice Garden', 'Indian', 'Manhattan', 4.2, '$$$');
INSERT INTO Restaurant VALUES (3, 'NYC Pizza House', 'Italian', 'Queens', 4.7, '$');
INSERT INTO Restaurant VALUES (4, 'Sakura Sushi', 'Japanese', 'Manhattan', 4.8, '$$$');
INSERT INTO Restaurant VALUES (5, 'Taco Town', 'Mexican', 'Bronx', 4.0, '$');
INSERT INTO Restaurant VALUES (6, 'Pasta Palace', 'Italian', 'Brooklyn', 4.3, '$$');

INSERT INTO MenuItem VALUES (1, 1, 'Classic Burger', 12.99, 'Main');
INSERT INTO MenuItem VALUES (2, 1, 'Fries', 4.99, 'Side');
INSERT INTO MenuItem VALUES (3, 2, 'Butter Chicken', 16.99, 'Main');
INSERT INTO MenuItem VALUES (4, 2, 'Garlic Naan', 3.99, 'Side');
INSERT INTO MenuItem VALUES (5, 3, 'Margherita Pizza', 10.99, 'Main');
INSERT INTO MenuItem VALUES (6, 4, 'Salmon Sushi', 18.99, 'Main');
INSERT INTO MenuItem VALUES (7, 5, 'Beef Taco', 8.99, 'Main');
INSERT INTO MenuItem VALUES (8, 6, 'Spaghetti Carbonara', 14.99, 'Main');

SELECT * FROM Restaurant ORDER BY Rating DESC;

SELECT Borough, COUNT(*) AS TotalRestaurants, AVG(Rating) AS AvgRating
FROM Restaurant
GROUP BY Borough
ORDER BY AvgRating DESC;

SELECT r.Name, m.Dish, m.Price
FROM Restaurant r
JOIN MenuItem m ON r.RestaurantID = m.RestaurantID
WHERE m.Category = 'Main'
ORDER BY m.Price ASC;

SELECT Cuisine, COUNT(*) AS Count
FROM Restaurant
GROUP BY Cuisine
ORDER BY Count DESC;

SELECT r.Name, r.Rating, r.Borough
FROM Restaurant r
WHERE r.Rating >= 4.5
ORDER BY r.Rating DESC;
