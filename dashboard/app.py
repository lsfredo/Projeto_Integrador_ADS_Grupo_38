import streamlit as st
import pandas as pd

st.title("🎧 Dashboard Spotify")

df = pd.read_csv("data/spotify.csv")

st.write(df.head())
