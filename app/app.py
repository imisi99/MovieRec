import streamlit as st
import requests

url = "http://127.0.0.1:8000"
st.header("Netflix movie recommendation")

st.write("This will recommend movies to based on your preferences.")

tags = requests.get(url+"/tags").json()
genre = tags[2]
country = tags[0]
rating = tags[1]

rating_ = st.multiselect(label="Select the rating of movie you prefer", options=rating)

genre_ = st.multiselect(label="Select the genre of movie you prefer", options=genre)

country_ = st.multiselect(label="Select the countries which movie you prefer", options=country)

Type = st.multiselect(label="Select the type of movie you prefer", options=["Movie", "TV Show"])

if st.button("Predict"):
    pass