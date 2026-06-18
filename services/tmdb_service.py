import requests

class TMDBService:

    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self, api_key):
        self.api_key = api_key


    def get_genres(self):

        url = f"{self.BASE_URL}/genre/movie/list"

        response = requests.get(
            url,
            params={"api_key": self.api_key}
        )

        return response.json()


    def discover_movies(self, genre, year):

        url = f"{self.BASE_URL}/discover/movie"

        response = requests.get(
            url,
            params={
                "api_key": self.api_key,
                "with_genres": genre,
                "primary_release_year": year
            }
        )

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