from flask import Flask
from flask import render_template
from flask import request

from dotenv import load_dotenv
import os

from services.tmdb_service import TMDBService
from recommender import MovieRecommender

import mysql.connector

# Connects to DB and keeps passwords/API keys safe
load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor(dictionary=True)

app = Flask(__name__)

tmdb = TMDBService(os.getenv("TMDB_API_KEY"))
logic = MovieRecommender()


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
        request.args.get("rating", 0)
    )

    genre_names = logic.MOOD_GENRES.get(
        mood.lower(),
        []
    )

    genre_ids = tmdb.genre_names_to_ids(
        genre_names
    )

    movies = tmdb.discover_movies(
        genre_ids,
        era
    )

    results = []

    for movie in movies["results"]:

        details = tmdb.get_movie_details(
            movie["id"]
        )

        if filter_movies(
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


@app.route("/movies")
def get_movies():
    cursor.execute("SELECT * FROM Movies")
    movies = cursor.fetchall()
    return {"movies": movies}


@app.route("/rate", methods=["POST"])
def add_rating():
    data = request.json

    cursor.execute("""
        INSERT INTO Ratings (user_id, movie_id, rating, review)
        VALUES (%s, %s, %s, %s)
    """, (
        data["user_id"],
        data["movie_id"],
        data["rating"],
        data.get("review", "")
    ))

    db.commit()
    return {"message": "Rating added"}


@app.route("/preferences/<int:user_id>", methods=["PUT"])
def update_preferences(user_id):
    data = request.json

    cursor.execute("""
        UPDATE UserPreferences
        SET streaming_provider = %s
        WHERE user_id = %s
    """, (
        data["streaming_provider"],
        user_id
    ))

    db.commit()
    return {"message": "Preferences updated"}


@app.route("/users/<int:user_id>/watchlist")
def get_watchlist(user_id):

    cursor.execute("""
        SELECT m.title, m.genre, m.streaming_provider
        FROM Watchlists w
        JOIN Movies m
        ON w.movie_id = m.movie_id
        WHERE w.user_id = %s
    """, (user_id,))

    return cursor.fetchall()


@app.route("/watchlist/<int:watchlist_id>", methods=["DELETE"])
def delete_watchlist_item(watchlist_id):

    cursor.execute("""
        DELETE FROM Watchlists
        WHERE watchlist_id = %s
    """, (watchlist_id,))

    db.commit()
    return {"message": "Deleted from watchlist"}


if __name__ == "__main__":
    app.run(debug=True)