class MovieRecommender:

    def mood_to_genre(self, mood):

        mood_map = {
            "happy": ["Comedy", "Family", "Animation"],
            "sad": ["Drama", "Musical", "Mystery"],
            "excited": ["Action", "Adventure", "Fantasy", "Mistery"],
            "relaxed": ["Family", "Documentary", "Romance", "History"],
            "restless": ["Crime", "Horror", "Thriller", "Science Fiction"]
        }

        genre_names = mood_map.get(mood)

        genres = self.get_genres()["genres"]

        genre_ids = []

        for genre in genres:

            if genre["name"] in genre_names:
                genre_ids.append(
                    str(genre["id"])
                )

        return ",".join(genre_ids)

    def filter_movie(
        self,
        details,
        min_duration,
        max_duration,
        duration,
        rating
    ):

        runtime = details["runtime"]
        vote = details["vote_average"]

        return (
            runtime <= duration
            and vote >= rating
        )