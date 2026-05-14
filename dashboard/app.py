import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Spotify", layout="wide")
st.title("🎧 Dashboard Spotify")

# agora usando a base tratada
df = pd.read_csv("data/spotify_tratado.csv")

# diagnóstico para descobrir as colunas
st.write("Linhas x Colunas:", df.shape)
st.write("Colunas:", list(df.columns))
st.write(df.head())

