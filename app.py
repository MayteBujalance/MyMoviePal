from flask import Flask
from flask import render_template
from flask import request

from services.tmdb_service import TMDBService
from services.recommender import MovieRecommender


app = Flask(__name__)

tmdb = TMDBService("bdf200e3f2bda51ec56715c004745a32")

logic = MovieRecommender()


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/recommend")

def recommend():

    mood = request.args.get("mood")

    era = request.args.get("era")

    duration = int(
        request.args.get("duration")
    )

    rating = float(
        request.args.get("rating")
    )

    genre = tmdb.mood_to_genre(mood)

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
            duration,
            rating
        ):

            results.append(details)


    return render_template(
        "results.html",
        movies=results
    )


if __name__ == "__main__":
    app.run(debug=True)