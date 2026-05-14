import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Spotify", layout="wide")
st.title("🎧 Dashboard Spotify")

# Agora o dashboard usa a base TRATADA
df = pd.read_csv("data/spotify_tratado.csv")

# Checagens rápidas (prova que carregou certo)
st.caption("Prévia da base tratada")
st.write("Linhas x Colunas:", df.shape)
st.write(df.head())
st.write("Colunas:", list(df.columns))

