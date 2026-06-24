from flask import Flask
from flask import render_template
from flask import request

from dotenv import load_dotenv
import os

from services.tmdb_service import TMDBService
from services.recommender import MovieRecommender


app = Flask(__name__)

# It keepo the API key safe
load_dotenv()

tmdb = TMDBService(os.getenv("TMDB_API_KEY"))


logic = MovieRecommender(tmdb) # suggested change to add arguemnt so recommender can access tmdb



@app.route("/")
def home():

    return render_template("index.html")


@app.route("/recommend")

def recommend():

    mood = request.args.get("mood")

    era = request.args.get("era")

    min_duration = int(request.args.get("min_duration", 0))
    max_duration = int(request.args.get("max_duration", 999))


    rating = float(
        request.args.get("rating")
    )

    genre = logic.mood_to_genre_ids(mood) # suggested change to fit with te class tmdb only needs to connect with the api)

    movies = tmdb.discover_movies(
        genre,
        era
    )


    results = []

    for movie in movies["results"]:

        details = tmdb.get_movie_details(
            movie["id"]
        )

        if logic.filter_movie(
                details,
                min_duration,
                max_duration,
                rating
        ):

            results.append(details)


    return render_template(
        "results.html",
        movies=results
    )


if __name__ == "__main__":
    app.run(debug=True)