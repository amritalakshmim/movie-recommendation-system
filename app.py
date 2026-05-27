import streamlit as st
from movie_recommender import recommend

st.title("Movie Recommendation System")

movie = st.text_input("Enter movie name:")

if st.button("Recommend"):

    recommendations = recommend(movie)

    for rec in recommendations:
        st.write(rec)
       