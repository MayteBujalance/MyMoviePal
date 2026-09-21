# 🎬 MyMoviePal

> Helping you spend less time searching and more time watching.

## 📖 Overview

After a long week, choosing a movie should be the easiest part of your evening. Instead, many of us find ourselves scrolling endlessly through streaming platforms, overwhelmed by thousands of options and unsure what to watch.

**MyMoviePal** is a movie recommendation application designed to solve this problem. By asking users a series of personalised questions, the application generates tailored movie recommendations based on their preferences, mood, and viewing criteria.

Unlike individual streaming services that only recommend content from their own platforms, MyMoviePal aims to provide recommendations from multiple streaming providers, giving users a broader range of options and helping them discover the perfect film faster.

---

## 🎯 Project Goal

The goal of MyMoviePal is to:

- Reduce the time users spend searching for a movie.
- Provide personalised movie recommendations.
- Aggregate movie information from multiple streaming platforms.
- Display where a movie is available to watch.
- Indicate whether a movie is:
  - Free to watch
  - Included in an existing subscription
  - Available through rental or purchase.
- Create an enjoyable and intuitive user experience.

---

## ✨ Features

### Current Features

- User questionnaire to collect movie preferences (mood, genre, duration, era and streaming provider)
- Recommendation engine powered by TMDB API
- Filtering by genre, release year, runtime and streaming provider
- Watchlist functionality
- Rating and review system
- Database integration for data persistence 
- Movie information display.

### Planned Features

- User accounts and saved favourites.
- Friend and group recommendations.
- Movie night / watch party mode.
- Recommendation history.
- Age rating filtering.

---

## 🛠️ Technologies Used

- Python
- Flask
- MySQL
- TMDB API
- InquirerPy
- Git & GitHub

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/MayteBujalance/MyMoviePal.git
cd MyMoviePal
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a .env file using the .env.example template provided and fill in 
your own values including your TMDB API key and local MySQL credentials.

### Set Up the Database
Run `my_movie_pal_database.sql` in dBeaver to create the database and tables.

### Run the Application

Open a terminal and run:
```bash
python3 main.py
```
---

## 📂 Project Structure

```text
MyMoviePal/
│
├── services/
├── app.py
├── main.py
├── questionnaire.py
├── recommender.py
├── my_movie_pal_database.sql
├── requirements.txt
├── README.md
└── .gitignore
└── .env.example
```
---

## 💡 How It Works

1. The user launches the application.
2. The application asks a series of questions about:
   - Preferred genres
   - Mood
   - Viewing preferences
   - Runtime
   - Streaming availability
3. User responses are analysed.
4. The recommendation engine matches responses against movie data.
5. A curated list of movie recommendations is presented.
6. The user can view where each movie is available to stream.

---

## 👥 Team Members

- Katie John
- Laura Dolan
- Mayte Bujalance Casas
- Omoefe Osayi
- Palvi Williams
- Tayibah Hussain

---

## 🔮 Future Improvements

- AI-powered recommendations.
- Personalised user profiles.
- Watch party integration.
- Mobile application support.
- Rating and review system.
- Integration with additional streaming providers.
- Machine learning recommendation engine.

---

## 📅 Project Status

🚧 **Currently in Development**

The project is currently in development, with features and documentation continuing to evolve.

---

## 🤝 Contributing

This repository is maintained by Group Six. Team members are encouraged to create feature branches and submit pull requests for review before merging changes into the main branch.

---

## 📜 License

This project is intended for educational purposes as part of the Degree programme.

---

## 🌟 Vision

Our vision is to create a single, user-friendly platform that removes the frustration of choosing a movie. MyMoviePal helps users discover films tailored to their tastes while providing transparency around where and how each title can be watched.
