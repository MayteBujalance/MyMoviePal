import unittest
from questionnaire import UserQuestionnaire

# Unit tests for the UserQuestionnair
class TestUserQuestionnaire(unittest.TestCase):

    # checks the class can be created without any issues
    def test_questionnaire_exists(self):
        q = UserQuestionnaire()
        self.assertIsNotNone(q)

    # checks the mood question method is there
    def test_get_mood_exists(self):
        q = UserQuestionnaire()
        self.assertTrue(hasattr(q, 'get_mood'))

    # checks the genre question method is there
    def test_get_genre_exists(self):
        q = UserQuestionnaire()
        self.assertTrue(hasattr(q, 'get_genre'))

    # checks the duration question method is there
    def test_get_duration_exists(self):
        q = UserQuestionnaire()
        self.assertTrue(hasattr(q, 'get_duration'))

    # checks the era question method is there
    def test_get_era_exists(self):
        q = UserQuestionnaire()
        self.assertTrue(hasattr(q, 'get_era'))

    # checks the streaming question method is there
    def test_get_streaming_exists(self):
        q = UserQuestionnaire()
        self.assertTrue(hasattr(q, 'get_streaming'))

    # checks the run method is there to kick everything off
    def test_run_exists(self):
        q = UserQuestionnaire()
        self.assertTrue(hasattr(q, 'run'))

if __name__ == "__main__":
    unittest.main()
