-- Створення таблиці Users

DROP TABLE Views;
DROP TABLE Videos;
DROP TABLE Genres;
DROP TABLE Users;

DROP TABLE Subscriptions;

CREATE TABLE Subscriptions (
    SubscriptionID INT PRIMARY KEY AUTO_INCREMENT,
    Type VARCHAR(50),
    Price DECIMAL(10, 2)
);


CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Email VARCHAR(100) UNIQUE,
    Password VARCHAR(100),
    SubscriptionID INT,
    FOREIGN KEY (SubscriptionID) REFERENCES Subscriptions(SubscriptionID)
);

CREATE TABLE Genres (
    GenreID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50)
);

-- Створення таблиці Videos
CREATE TABLE Videos (
    VideoID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(200),
    Description VARCHAR(500),
    GenreID INT,
    Duration INT,
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID)
);

-- Створення таблиці Subscriptions

-- Створення таблиці Views
CREATE TABLE Views (
    ViewID INT PRIMARY KEY AUTO_INCREMENT,
    UserID INT,
    VideoID INT,
    ViewDate DATETIME,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (VideoID) REFERENCES Videos(VideoID)
);

-- Створення таблиці Genres
-- Вставка даних у таблицю Genres
INSERT INTO Genres (Name) VALUES ('Drama'), ('Comedy'), ('Sci-Fi'), ('Horror'), ('Documentary');

-- Вставка даних у таблицю Subscriptions
INSERT INTO Subscriptions (Type, Price) VALUES 
('Basic', 7.99), 
('Premium', 12.99), 
('Family', 15.99), 
('Student', 5.99), 
('Ultimate', 19.99);

-- Вставка даних у таблицю Videos
INSERT INTO Videos (Title, Description, GenreID, Duration) VALUES 
('Movie 1', 'Description for Movie 1', 1, 120),
('Movie 2', 'Description for Movie 2', 2, 90),
('Movie 3', 'Description for Movie 3', 3, 140),
('Movie 4', 'Description for Movie 4', 4, 105),
('Movie 5', 'Description for Movie 5', 5, 80);

-- Вставка даних у таблицю Users
INSERT INTO Users (Name, Email, Password, SubscriptionID) VALUES 
('John Smith', 'john@example.com', 'password123', 1),
('Mariia Ivanova', 'mariia@example.com', 'mariiapass', 2),
('Anastasia Petrova', 'anastasia@example.com', 'anapass', 3),
('Anna Johnson', 'anna@example.com', 'annapass', 4),
('Michael Brown', 'michael@example.com', 'mikepass', 5);

-- Вставка даних у таблицю Views
INSERT INTO Views (UserID, VideoID, ViewDate) 
VALUES 
(1, 1, '2024-10-01'), 
(2, 2, '2024-10-03'), 
(3, 3, '2024-10-05'), 
(4, 4, '2024-10-02'), 
(5, 5, '2024-10-04');



SELECT * FROM Genres;
SELECT * FROM Subscriptions;
SELECT * FROM Videos;
SELECT * FROM Users;
SELECT * FROM Views;
