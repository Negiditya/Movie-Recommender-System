# 🎬 Movie Recommender System

A content-based movie recommendation system that suggests similar movies
using cosine similarity on textual features such as genres, keywords, overview
cast, and crew.

🔗 **Live Demo:** (https://movie-recommender-system-r993.onrender.com)

------------------------------------------------------------------------

## 🚀 Features

-   Recommends Top 5 similar movies instantly
-   Content-based filtering using cosine similarity
-   Movie poster fetching using TMDB API
-   Optimized similarity matrix (Top 20 per movie) for fast performance


------------------------------------------------------------------------

## 🧠 How It Works

1. Important features (genres, keywords, cast, crew, overview) are combined.
2. Text is vectorized using Count Vectorization.
3. Cosine similarity is computed between movie vectors.
4. For performance optimization, only the Top 20 similar movies per movie are stored.
5. When a user selects a movie, the system returns the Top 5 most similar movies.

------------------------------------------------------------------------

## 📊 Dataset

This project uses the TMDB Movie Metadata dataset:

-   Kaggle TMDB Dataset\
    https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Movie posters are fetched dynamically using the TMDB API.

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python
-   Streamlit
-   Pandas
-   NumPy
-   Scikit-learn
-   Requests
-   TMDB API

------------------------------------------------------------------------

## 📁 Project Structure

movie-recommender-system/ │ ├── app.py ├── movies.pkl ├──
top_20_similar_movies.pkl ├── requirements.txt ├── notebooks/ │ └──
data_preprocessing_and_similarity_model.ipynb
