from enum import global_enum_repr

from InquirerPy import inquirer

# Handles the user questionnaire flow for MyMoviePal
class UserQuestionnaire:

    # Asks the user how they're feeling
    def get_mood(self):
        mood = inquirer.select(
            message="How are you feeling?",
            choices=[
                "😊Happy - I want somthing fun and uplifting",
                "😢Sad - I need a good cry",
                "😱Tense - I want something thrilling",
                "🤔Thoughtful - I'm in the mood for something deep",
                "😴Chilled - Something easy to watch"
            ]
        ).execute()

        # Confirms the user is happy with their choice
        confirm = inquirer.confirm(
            message=f"You chose '{mood}', is this correct?"
            ).execute()

        # If not happy, asks again
        if not confirm:
            return self.get_mood()

        return mood

    # Asks the user which genre they want
    def get_genre(self):
        genre = inquirer.select(
            message="What genre are you in the mood for?",
            choices=[
                "Comedy",
                "Drama",
                "Action",
                "Horror",
                "Romance",
                "Thriller",
                "Documentary",
                "Sci-Fi",
                "Animation",
            ]
        ).execute()

        # Confirms the user is happy with their choice
        confirm = inquirer.confirm(
            message=f"You chose '{genre}', is this correct?"
        ).execute()

        # If not happy, asks again
        if not confirm:
            return self.get_genre()

        return genre

    # Asks the user how long they have
    def get_duration(self):
        duration = inquirer.select(
            message="How long do you have?",
            choices=[
            "Short (under 90mins)",
            "Standard (90-120mins)",
            "Epic (2hrs+)"
            ]
        ).execute()

        # Confirms the user is happy with their choice
        confirm = inquirer.confirm(
            message=f"You chose '{duration}', is this correct?"
        ).execute()

        # If not happy, asks again
        if not confirm:
            return self.get_duration()

        return duration

    # Asks the user which era they want
    def get_era(self):
        era = inquirer.select(
            message="What era are you feeling?",
            choices=[
            "Classic (pre 1990)",
            "90s/2000s",
            "Modern (2010s)",
            "Latest releases"
            ]
        ).execute()

        # Confirms the user is happy with their choice
        confirm = inquirer.confirm(
            message=f"You chose '{era}', is this correct?"
        ).execute()

        # If not happy, asks again
        if not confirm:
            return self.get_era()

        return era

    # Asks the user which how they're watching e.g. streaming service
    def get_streaming(self):
        streaming = inquirer.select(
            message="Where are you watching tonight?",
            choices=[
            "Netflix",
            "Amazon Prime Video",
            "Disney+",
            "Apple TV+",
            "I dont mind"
            ]
        ).execute()

        # Confirms the user is happy with their choice
        confirm = inquirer.confirm(
            message=f"You chose '{streaming}', is this correct?"
        ).execute()

        # If not happy, asks again
        if not confirm:
            return self.get_streaming()

        return streaming

# Runs through all the questions and returns the users answers
    def run(self):
        try:
            print("\n🎬Welcome to MyMoviePal!")
            print("Answer a few questions and we'll find your perfect film!\n")

            mood = self.get_mood()
            genre = self.get_genre()
            duration = self.get_duration()
            era = self.get_era()
            streaming = self.get_streaming()

            print(f"\n🎬Great choices! Finding your perfect film...\n")

            return mood, genre, duration, era, streaming

        # created if users wish to exit the questionnaire early
        except KeyboardInterrupt:
            print("\n\nNo worries, come back when you're ready! 🎬")
        # created to catch unexpected errors to prevent the app from crashing
        except Exception as e:
            print(f"\nSomething went wrong: {e}")

# Kicks things off
questionnaire = UserQuestionnaire()
questionnaire.run()
