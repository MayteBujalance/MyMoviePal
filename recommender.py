from datetime import datetime

class MovieRecommender:

    MOOD_GENRES = {
        "happy" : ["Adventure", "Animation", "Comedy", "Family"],
        "sad" : ["Drama", "Romance"],
        "tense": ["Action", "Horror", "Thriller"],
        "thoughtful": ["Documentary", "Drama", "Science Fiction"],
        "chilled": ["Animation", "Comedy", "Family", "Romance"]
    }
    
    # Movie lengths ranging up to 4 hours are the standard movie length.
    def find_movie_duration(self, duration_length):
        if duration_length == "short":
            return 0, 90
        elif duration_length == "standard":
            return 90, 120
        elif duration_length == "long":
            return 120, 240
        else:
            return 0, 999

    # These were the most popular era categories discussed for movies.
    def find_movie_era(self, era_selection):
        if era_selection == "classic":
            return "1900-01-01", "1989-12-31"
        elif era_selection == "90s_2000s":
            return "1990-01-01", "2009-12-31"
        elif era_selection == "modern":
            return "2010-01-01", "2019-12-31"
        elif era_selection == "newest":
            return "2020-01-01", "2030-12-31"
        else:
            return "1900-01-01", "2030-12-31"

    # This is the recommendation filter part, using Boolean values to see if the movies listed
    # match the user's criteria.
    
    def filter_movies(self, details, min_duration, max_duration, rating):
       runtime = details.get("runtime")
       vote = details.get("vote_average")

       if runtime is None or vote is None:
           return False

        return(
            runtime >= min_duration
            and runtime <= max_duration
            and vote >= rating
            )
