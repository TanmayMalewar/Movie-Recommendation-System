import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Page settings
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬"
)

st.title("🎬 Movie Recommendation System")
st.write("Find movies similar to your favorite movie.")


# Load datasets
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

movies = pd.read_csv(
    BASE_DIR / "dataset" / "movies.csv"
)


# Prepare genres
movies["genres"] = movies["genres"].fillna("")


# Convert genres into TF-IDF vectors
vectorizer = TfidfVectorizer(
    stop_words="english"
)

vectors = vectorizer.fit_transform(
    movies["genres"]
)


# Recommendation function
def recommend(movie_title):

    movie_index = movies[
        movies["title"] == movie_title
    ].index

    if len(movie_index) == 0:
        return []

    movie_index = movie_index[0]

    # Calculate similarity ONLY for the selected movie
    similarity_scores = cosine_similarity(
        vectors[movie_index],
        vectors
    ).flatten()

    # Get top 5 similar movies
    similar_indices = similarity_scores.argsort()[-6:][::-1]

    recommendations = []

    for index in similar_indices:

        if index != movie_index:
            recommendations.append(
                movies.iloc[index]["title"]
            )

        if len(recommendations) == 5:
            break

    return recommendations


# Movie selection
movie_list = movies["title"].dropna().tolist()

selected_movie = st.selectbox(
    "🎥 Select a movie:",
    movie_list
)


# Recommendation button
if st.button("🍿 Recommend Movies"):

    recommendations = recommend(
        selected_movie
    )

    st.subheader("🎬 Recommended Movies")

    for i, movie in enumerate(
        recommendations,
        1
    ):
        st.write(
            f"**{i}. {movie}**"
        )