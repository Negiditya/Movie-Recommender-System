import streamlit as st

import pickle
import requests
import os
from dotenv import load_dotenv

st.set_page_config(layout="wide")
load_dotenv()



with open("movies.pkl", "rb") as f:
    movies_df = pickle.load(f)

with open("top_20_similar_movies.pkl", "rb") as f:
    similarity = pickle.load(f)


@st.cache_data(show_spinner=False)
def fetch_posters(movie_ids):

    api_key = os.getenv("TMDB_API_KEY")
    
    posters = []
    for id in movie_ids:
        url = f"https://api.themoviedb.org/3/movie/{id}?api_key={api_key}"
        data = requests.get(url)
        posters.append("https://image.tmdb.org/t/p/w500/" + data.json()["poster_path"])

    return posters


def recommend_movies(movie):

    movie_idx = movies_df[movies_df["title"] == movie].index[0]
    top_movies_idxs = similarity[movie_idx][0:5]
    recommend_movies = movies_df["title"].iloc[top_movies_idxs].tolist()
    movie_ids = movies_df["id"].iloc[top_movies_idxs].tolist()
    posters = fetch_posters(movie_ids)
    return recommend_movies, posters


st.title("Movie Recommender System")


movie = st.selectbox("Enter the movie name", movies_df["title"])


if st.button("Recommend"):
    with st.spinner("getting recommendations..."):
        titles, posters = recommend_movies(movie)

    cols = st.columns(5, gap ="large")

    for i in range(len(titles)):
        with cols[i]:
            st.image(posters[i])
            st.text(titles[i])
