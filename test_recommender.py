import unittest
from recommender import MovieRecommender

# unit test for the MovieRecommender
class TestMovieRecommender(unittest.TestCase):

     #checks if the class can exists without issues
    def test_MovieRecommender_exists(self):
        r = MovieRecommender()
        self.assertIsNotNone(r)


    #checks if the movie duration exists
    def test_find_movie_duration_exists(self):
        r = MovieRecommender()
        self.assertTrue(hasattr(r, "find_movie_duration"))


    #checks if the find movie exists
    def test_find_movie_era(self):
        r = MovieRecommender()
        self.assertTrue(hasattr(r, "find_movie_era"))


if __name__ == "__main__":
    unittest.main()
