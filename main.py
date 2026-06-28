import os
from dotenv import load_dotenv
import mysql.connector

from questionnaire import UserQuestionnaire
from recommender import MovieRecommender
from services.tmdb_service import TMDBService


def save_user_preferences(user_id, mood, genre, duration, era, streaming):
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO UserPreferences (
            user_id,
            mood,
            genre,
            duration,
            era,
            streaming_provider
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        user_id,
        mood,
        genre,
        duration,
        era,
        streaming
    ))

    db.commit()
    cursor.close()
    db.close()


def main():
    load_dotenv()

    api_key = os.getenv("TMDB_API_KEY")

    if not api_key:
        print("TMDB API key not found. Please check your .env file.")
        return

    questionnaire = UserQuestionnaire()
    mood, genre, duration, era, streaming = questionnaire.run()

    save_user_preferences(
        1,
        mood,
        genre,
        duration,
        era,
        streaming
    )

    print("✅ Your preferences have been saved.")

    tmdb = TMDBService(api_key)
    recommender = MovieRecommender()

    genre_names = recommender.MOOD_GENRES.get(mood.lower(), [])

    if genre:
        genre_names.append(genre.title())

    genre_ids = tmdb.genre_names_to_ids(genre_names)

    movies = tmdb.discover_movies(
        genre_ids,
        era
    )

    min_duration, max_duration = recommender.find_movie_duration(
        duration
    )

    recommendations = []

    for movie in movies["results"]:

        details = tmdb.get_movie_details(
            movie["id"]
        )

        if recommender.filter_movies(
            details,
            min_duration,
            max_duration,
            0
        ):
            recommendations.append(details)

    print("\n🎬 Here are your recommendations:\n")

    if not recommendations:
        print("Sorry, no recommendations found. Try changing your answers.")
        return

    for movie in recommendations[:5]:

        print(movie["title"])
        print(f"Runtime: {movie.get('runtime')} minutes")
        print(f"Rating: {movie.get('vote_average')}")
        print(f"Overview: {movie.get('overview')}")
        print("-" * 40)


if __name__ == "__main__":
    main()