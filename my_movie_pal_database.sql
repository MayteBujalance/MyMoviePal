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
    
INSERT INTO Movies(tmdb_id, title, release_date, genre, runtime, vote_average, main_actor, streaming_provider, overview, poster_path)
VALUES(
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
),

(
301528,
'Toy Story 4',
'2019-06-19',
'Animation, Family, Comedy, Adventure',
100,
7.50,
'Tom Hanks',
'Disney+',
'Woody and the gang embark on a road trip adventure after meeting a new toy called Forky.',
'/w9kR8qbmQ01HwnvK4alvnQ2ca0L.jpg'
),

(
496243,
'Parasite',
'2019-05-30',
'Drama, Thriller, Comedy',
132,
8.50,
'Song Kang-ho',
'Amazon Prime Video',
'A poor family gradually infiltrates the lives of a wealthy household with unexpected consequences.',
'/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg'
),

(
269149,
'Zootopia',
'2016-02-11',
'Animation, Adventure, Comedy, Family',
108,
7.80,
'Ginnifer Goodwin',
'Disney+',
'A rookie rabbit police officer teams up with a fox to solve a mystery.',
'/hlK0e0wAQ3VLuJcsfIYPvb4JVud.jpg'
),

(
177572,
'Big Hero 6',
'2014-10-24',
'Animation, Action, Adventure, Family',
102,
7.70,
'Ryan Potter',
'Disney+',
'A young robotics prodigy teams up with Baymax and friends to fight crime.',
'/2mxS4wUimwlLmI1xp6QW6NSU361.jpg'
),

(
293660,
'Deadpool',
'2016-02-09',
'Action, Comedy, Adventure',
108,
7.60,
'Ryan Reynolds',
'Disney+',
'A former special forces operative becomes the wisecracking mercenary Deadpool.',
'/3E53WEZJqP6aM84D8CckXx4pIHw.jpg'
),

(
10192,
'Shrek Forever After',
'2010-05-20',
'Animation, Adventure, Comedy, Family',
93,
6.40,
'Mike Myers',
'Netflix',
'Shrek makes a deal that turns his world upside down.',
'/6HrfPZtKcGmX2tUWW3cnciZTaSD.jpg'
),

(
106646,
'The Wolf of Wall Street',
'2013-12-25',
'Drama, Comedy, Crime',
180,
8.00,
'Leonardo DiCaprio',
'Netflix',
'A New York stockbroker becomes involved in fraud, corruption and excess.',
'/kW9LmvYHAaS9iA0tHmZVq8hQYoq.jpg'
);

INSERT INTO UserPreferences
(user_id, mood, genre, duration, era, streaming_provider)
VALUES
(1, 'relaxed', 'Science Fiction', 'Long', '2010s', 'Amazon Prime'),

(2, 'happy', 'Animation', 'Medium', '2010s', 'Disney+'),

(3, 'restless', 'Thriller', 'Long', '2010s', 'Amazon Prime Video'),

(4, 'relaxed', 'Animation', 'Medium', '2010s', 'Disney+'),

(5, 'excited', 'Action', 'Medium', '2010s', 'Disney+'),

(6, 'happy', 'Comedy', 'Medium', '2010s', 'Disney+'),

(7, 'relaxed', 'Animation', 'Short', '2010s', 'Netflix'),

(8, 'excited', 'Drama', 'Long', '2010s', 'Netflix'),

(9, 'relaxed', 'Science Fiction', 'Long', '2010s', 'Amazon Prime'),

(10, 'restless', 'Drama', 'Long', '2010s', 'Amazon Prime Video');


INSERT INTO Watchlists (user_id, movie_id)
VALUES
(1,1),
(1,8),

(2,2),
(2,5),

(3,3),
(3,6),

(4,1),
(4,3),

(5,2),
(5,4),

(6,6),
(6,8),

(7,5),
(7,2),

(8,7),
(8,5),

(9,1),
(9,8),

(10,3),
(10,4);

INSERT INTO Ratings
(user_id, movie_id, rating, review)
VALUES
(1, 1, 5, 'One of the best sci-fi films ever made'),
(1, 5, 5, 'Baymax was hilarious and heartwarming'),

(2, 2, 4, 'A fun and emotional ending to the Toy Story series'),
(2, 3, 5, 'Brilliant story with an unexpected ending'),

(3, 3, 5, 'Kept me hooked from start to finish'),
(3, 4, 4, 'Loved the characters and humour'),

(4, 1, 5, 'Mind-blowing concept and execution'),
(4, 5, 4, 'Great animation and action scenes'),

(5, 2, 5, 'Perfect family movie'),
(5, 4, 4, 'A very entertaining mystery adventure'),

(6, 1, 4, 'Excellent movie with a clever plot'),
(6, 6, 5, 'Deadpool is hilarious and action-packed'),

(7, 5, 5, 'One of Disneys best modern films'),

(8, 2, 4, 'Really enjoyed the new characters'),
(8, 7, 4, 'Funny and nostalgic'),
(8, 5, 5, 'Baymax stole the show'),

(9, 1, 5, 'A masterpiece'),
(9, 8, 5, 'Incredible performance by Leonardo DiCaprio'),

(10, 3, 4, 'Very well written'),
(10, 4, 5, 'Loved the world and characters');


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


   
