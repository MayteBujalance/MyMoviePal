from datetime import datetime

class MovieRecommender:

    MOVIE_MOODS = {
        "happy" : ["Adventure", "Animation", "Comedy", "Family"],
        "sad" : ["Drama", "Romance"],
        "tense": ["Action", "Horror", "Thriller"],
        "thoughtful": ["Documentary", "Drama", "Sci-Fi"],
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

    def mood_movie_match(self, movie_genre, mood):
        current_genres = self.MOVIE_MOODS.get(mood.lower(), [])
        return movie_genre in current_genres

    def movie_choice_filtering(self, movie, user_filter):
        movie_genre = movie.get("genre")
        movie_duration = movie.get("duration")
        movie_rating = movie.get("rating")
        movie_release_date = movie.get("release_date")
        mood = user_filter.get("mood")
        genre_choice = user_filter.get("genre")
        duration_minimum = user_filter.get("min_duration")
        duration_maximum = user_filter.get("max_duration")
        lowest_movie_rating = user_filter.get("rating")

        # In case any data has been missed
        if movie_duration is None or movie_rating is None:
            return False

        # Now to check the mood
        if mood and not self.mood_movie_match(movie_genre, mood):
            return False

        # On to genres
        if genre_choice and movie_genre != genre_choice:
            return False

        # Now to check duration
        if movie_duration < duration_minimum or movie_duration > duration_maximum:
            return False


        if movie_rating < lowest_movie_rating:
            return False

        return True



