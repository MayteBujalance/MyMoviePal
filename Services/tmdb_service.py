import requests


class TMDBService:
    """
    Handles communication with the TMDB API.
    """

    def mood_to_genre(self, mood):
        mood_mapping = {
            "happy": 35,  # Comedy
            "sad": 18,  # Drama
            "tense": 53,  # Thriller
            "thoughtful": 99,  # Documentary
            "chilled": 16  # Animation
        }

        return mood_mapping.get(mood.lower())

    def discover_movies(self, genre, era):
        url = f"{self.BASE_URL}/discover/movie"

        params = {
            "api_key": self.api_key,
            "with_genres": genre,
            "sort_by": "vote_average.desc",
            "vote_count.gte": 100
        }

        if era == "classic":
            params["primary_release_date.lte"] = "1989-12-31"
        elif era == "90s_2000s":
            params["primary_release_date.gte"] = "1990-01-01"
            params["primary_release_date.lte"] = "2009-12-31"
        elif era == "modern":
            params["primary_release_date.gte"] = "2010-01-01"
            params["primary_release_date.lte"] = "2019-12-31"
        elif era == "latest":
            params["primary_release_date.gte"] = "2020-01-01"

        response = requests.get(url, params=params)

        return response.json()

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