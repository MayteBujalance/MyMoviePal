class TMDBService:
    """
    Handles communication with the TMDB API.
    """

    def mood_to_genre(self, mood):
        """
        Converts a user mood into a TMDB genre.
        Example:
        Happy -> Comedy
        Sad -> Drama
        """
        mood_mapping = {
            "happy": 35,        # Comedy
            "sad": 18,          # Drama
            "tense": 53,        # Thriller
            "thoughtful": 99,   # Documentary
            "chilled": 16       # Animation
        }

        return mood_mapping.get(mood.lower())

    def discover_movies(self, genre, era):
        """
        Uses TMDB Discover endpoint to find movies
        matching genre and era.
        """
        pass

    def get_movie_details(self, movie_id):
        """
        Returns runtime, rating, overview etc.
        """
        pass

    def get_movie_cast(self, movie_id):
        """
        Returns cast information.
        """
        pass

    def get_watch_providers(self, movie_id):
        """
        Returns streaming providers.
        """
        pass

    def get_genres(self):
        """
        Returns TMDB genre list.
        """
        pass