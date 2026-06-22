import requests


class TMDBService:
    """
    Handles communication with the TMDB API.
    """

    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self, api_key):
        self.api_key = api_key

    def mood_to_genre(self, mood):
        mood_mapping = {
            "happy": 35,        # Comedy
            "sad": 18,          # Drama
            "tense": 53,        # Thriller
            "thoughtful": 99,   # Documentary
            "chilled": 16       # Animation
        }

        if mood is None:
            return None

        return mood_mapping.get(mood.lower())

    def get_genres(self):
        url = f"{self.BASE_URL}/genre/movie/list"

        response = requests.get(
            url,
            params={"api_key": self.api_key}
        )

        return response.json()

    def discover_movies(self, genre, era):
        url = f"{self.BASE_URL}/discover/movie"

        params = {
            "api_key": self.api_key,
            "with_genres": genre,
            "sort_by": "popularity.desc"
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
        url = f"{self.BASE_URL}/movie/{movie_id}"

        response = requests.get(
            url,
            params={"api_key": self.api_key}
        )

        return response.json()

    def get_movie_cast(self, movie_id):
        url = f"{self.BASE_URL}/movie/{movie_id}/credits"

        response = requests.get(
            url,
            params={"api_key": self.api_key}
        )

        return response.json()

    def get_watch_providers(self, movie_id):
        url = f"{self.BASE_URL}/movie/{movie_id}/watch/providers"

        response = requests.get(
            url,
            params={"api_key": self.api_key}
        )

        return response.json()