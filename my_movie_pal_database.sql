CREATE DATABASE MyMoviePal;
USE MyMoviePal;

CREATE TABLE Users(
user_id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(50) NOT NULL UNIQUE,
email VARCHAR(100) NOT NULL UNIQUE,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Movies(
movie_id INT AUTO_INCREMENT PRIMARY KEY,
tmdb_id INT NOT NULL UNIQUE,
title VARCHAR(255) NOT NULL,
release_date DATE,
genre VARCHAR(255),
runtime INT,
vote_average DECIMAL(4,2),
main_actor VARCHAR(255),
streaming_provider VARCHAR(255),
overview TEXT,
poster_path VARCHAR(255)
);

CREATE TABLE UserPreferences(
preference_id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT NOT NULL,
mood VARCHAR(100),
genre VARCHAR(100),
duration VARCHAR(100),
era VARCHAR(100),
streaming_provider VARCHAR(255),
FOREIGN KEY(user_id) REFERENCES Users(user_id)
);

CREATE TABLE Watchlists(
watchlist_id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT NOT NULL,
movie_id INT NOT NULL,
added_at DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(user_id) REFERENCES Users(user_id),
FOREIGN KEY(movie_id) REFERENCES Movies(movie_id)
);

CREATE TABLE Ratings(
rating_id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT NOT NULL,
movie_id INT NOT NULL,
rating INT NOT NULL CHECK(rating BETWEEN 1 AND 5),
review TEXT,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(user_id) REFERENCES Users(user_id),
FOREIGN KEY(movie_id) REFERENCES Movies(movie_id)
);

CREATE TABLE Follows(
follow_id INT AUTO_INCREMENT PRIMARY KEY,
follower_id INT NOT NULL,
following_id INT NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(follower_id) REFERENCES Users(user_id),
FOREIGN KEY(following_id) REFERENCES Users(user_id)
);

INSERT INTO Users (username, email)
VALUES
('moviebuff22', 'moviebuff22@email.com'),
('scifiexplorer', 'scifiexplorer@email.com'),
('actionaddict', 'actionaddict@email.com'),
('cinemalover', 'cinemalover@email.com'),
('fantasyfan', 'fantasyfan@email.com'),
('thrillseeker', 'thrillseeker@email.com'),
('bingequeen', 'bingequeen@email.com'),
('watchparty', 'watchparty@email.com'),
('filmcritic', 'filmcritic@email.com'),
('popcornlover', 'popcornlover@email.com');
    
INSERT INTO Movies
(tmdb_id, title, release_date, genre, runtime, vote_average, main_actor, streaming_provider, overview, poster_path)
VALUES
(
27205,
'Inception',
'2010-07-15',
'Action, Science Fiction, Adventure',
148,
8.37,
'Leonardo DiCaprio',
'Amazon Prime',
'Cobb, a skilled thief who commits corporate espionage by infiltrating the subconscious of his targets.',
'/xlaY2zyzMfkhk0HSC5VUwzoZPU1.jpg'
);

INSERT INTO Movies
(tmdb_id, title, release_date, genre, runtime, vote_average, main_actor, streaming_provider, overview, poster_path)
VALUES
(
130799,
'Divergent',
'2014-03-21',
'Science Fiction, Adventure, Romance',
139,
6.90,
'Shailene Woodley',
'Netflix',
'In a society divided into factions, Tris discovers she is Divergent and uncovers a dangerous conspiracy.',
'/jIK4zYCMpD7zqZK4g6N8Y6S7hzM.jpg'
);

INSERT INTO Movies
(tmdb_id, title, release_date, genre, runtime, vote_average, main_actor, streaming_provider, overview, poster_path)
VALUES
(
198663,
'The Maze Runner',
'2014-09-19',
'Action, Mystery, Science Fiction',
113,
7.20,
'Dylan O''Brien',
'Disney+',
'Thomas wakes up trapped in a maze with no memory of his past and must work with others to escape.',
'/ode14q7WtDugFDp78fo9lCsmay9.jpg'
);

INSERT INTO Movies
(tmdb_id, title, release_date, genre, runtime, vote_average, main_actor, streaming_provider, overview, poster_path)
VALUES
(
131634,
'The Hunger Games',
'2012-03-23',
'Science Fiction, Adventure, Action',
142,
7.20,
'Jennifer Lawrence',
'Netflix',
'Katniss Everdeen volunteers to take her sisters place in a televised fight for survival.',
'/iQK0pkTQC60XBUsNQJgg5DA0eFq.jpg'
);

INSERT INTO Movies
(tmdb_id, title, release_date, genre, runtime, vote_average, main_actor, streaming_provider, overview, poster_path)
VALUES
(
438631,
'Dune',
'2021-10-22',
'Science Fiction, Adventure, Drama',
155,
8.00,
'Timothee Chalamet',
'Now TV',
'Paul Atreides must travel to the most dangerous planet in the universe to secure the future of his family.',
'/d5NXSklXo0qyIYkgV94XAgMIckC.jpg'
);

INSERT INTO UserPreferences (user_id, mood, genre, duration, era, streaming_provider)
VALUES
(1, 'Excited', 'Science Fiction', 'Long', '2010s', 'Netflix'),

(2, 'Adventurous', 'Action', 'Medium', '2010s', 'Disney+'),

(3, 'Curious', 'Mystery', 'Medium', '2010s', 'Disney+'),

(4, 'Thoughtful', 'Drama', 'Long', '2020s', 'Now TV'),

(5, 'Inspired', 'Adventure', 'Long', '2010s', 'Amazon Prime'),

(6, 'Energetic', 'Action', 'Long', '2010s', 'Netflix'),

(7, 'Relaxed', 'Science Fiction', 'Medium', '2020s', 'Now TV'),

(8, 'Excited', 'Adventure', 'Long', '2010s', 'Netflix'),

(9, 'Analytical', 'Science Fiction', 'Long', '2010s', 'Amazon Prime'),

(10, 'Happy', 'Action', 'Medium', '2010s', 'Disney+'); 


INSERT INTO Watchlists (user_id, movie_id)
 VALUES
 (1, 1),
 (1, 5),

 (2, 2),
 (2, 3),
 (2, 5),

 (3, 3),
 (3, 4),

 (4, 1),
 (4, 5),

 (5, 2),
 (5, 4),

 (6, 1),
 (6, 3),
 (6, 4),

 (7, 5),

 (8, 2),
 (8, 4),
 (8, 5),

 (9, 1),
 (9, 5),

 (10, 3),
 (10, 4);

INSERT INTO Ratings
 (user_id, movie_id, rating, review)
 VALUES
 (1, 1, 5, 'One of the best sci-fi films ever made'),
 (1, 5, 5, 'Amazing visuals and storytelling'),

 (2, 2, 4, 'Really enjoyed the faction system'),
 (2, 3, 5, 'Kept me hooked from start to finish'),

 (3, 3, 4, 'Great action and suspense'),
 (3, 4, 5, 'Loved Katniss as the main character'),

 (4, 1, 5, 'Mind-blowing concept'),
 (4, 5, 4, 'Beautiful cinematography'),

 (5, 2, 5, 'One of my favourite dystopian movies'),
 (5, 4, 4, 'Very entertaining'),

 (6, 1, 4, 'Excellent movie with a clever plot'),
 (6, 4, 5, 'Amazing adaptation of the book'),

 (7, 5, 5, 'Absolutely incredible world-building'),

 (8, 2, 4, 'Enjoyed the characters'),
 (8, 4, 5, 'Exciting from beginning to end'),
 (8, 5, 4, 'Great soundtrack and visuals'),

 (9, 1, 5, 'A masterpiece'),
 (9, 5, 5, 'One of the best films of the decade'),

 (10, 3, 4, 'Interesting concept'),
 (10, 4, 5, 'Would definitely watch again');


INSERT INTO Follows (follower_id, following_id)
 VALUES
 (1, 2),
 (1, 4),
 (1, 9),

 (2, 1),
 (2, 3),
 (2, 8),

 (3, 4),
 (3, 6),

 (4, 1),
 (4, 5),
 (4, 10),

 (5, 2),
 (5, 7),

 (6, 3),
 (6, 8),

 (7, 1),
 (7, 9),

 (8, 4),
 (8, 10),

 (9, 1),
 (9, 5),

 (10, 2),
 (10, 7);

 

-- TEST QUERIES

-- Show ratings with user and movie details
/* SELECT u.username, m.title, r.rating
FROM Ratings r
INNER JOIN Users u ON r.user_id = u.user_id
INNER JOIN Movies m ON r.movie_id = m.movie_id 
ORDER BY r.rating DESC; */

-- Show all movies, including movies with no ratings
/* SELECT m.title, COALESCE(AVG(r.rating), 0) AS average_rating
FROM Movies m
LEFT JOIN Ratings r ON m.movie_id = r.movie_id
GROUP BY m.movie_id, m.title; */

-- Count how many users have each movie in their watchlist
/* SELECT m.title, COUNT(w.watchlist_id) AS watchlist_count
FROM Movies m
LEFT JOIN Watchlists w ON m.movie_id = w.movie_id
GROUP BY m.movie_id, m.title
ORDER BY watchlist_count DESC; */

-- Show movies with an average rating greater than 4
/* SELECT m.title, AVG(r.rating) AS average_rating
FROM Ratings r
INNER JOIN Movies m ON r.movie_id = m.movie_id
GROUP BY m.movie_id, m.title
HAVING AVG(r.rating) > 4; */


   
