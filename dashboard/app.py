import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Spotify", layout="wide")
st.title("🎧 Dashboard Spotify")

# =========================
# 1) Carregar base tratada
# =========================
df = pd.read_csv("data/spotify_tratado.csv")

# =========================
# 2) Garantir tipos (robusto)
# =========================
df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")

df["inactive_3_months_flag"] = df["inactive_3_months_flag"].astype(str).str.lower().map(
    {"1": True, "0": False, "true": True, "false": False}
)

for c in ["ad_interaction", "ad_conversion_to_subscription"]:
    df[c] = (df[c].astype(str).str.lower().map({"yes": True,"no": False}))    

num_cols = [
    "age",
    "months_inactive",
    "music_suggestion_rating_1_to_5",
    "avg_listening_hours_per_week",
    "playlists_created",
    "avg_skips_per_day",
]
for c in num_cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")

# =========================
# 3) Filtros Interativos (Barra Lateral)
# =========================
st.sidebar.header("🔍 Filtrar Assinaturas")

opcoes_assinaturas = ["Todos"] + sorted(df["subscription_type"].dropna().unique())
filtro_assinatura = st.sidebar.selectbox("Tipo de Assinatura", opcoes_assinaturas)

# =========================
# 4) Aplicação dos Filtros
# =========================
if filtro_assinatura == "Todos":
    df_filtrado = df
else:
    df_filtrado = df[df["subscription_type"] == filtro_assinatura]

if df_filtrado.empty:
    st.warning("Nenhum dado para o filtro selecionado.")
    st.stop()

# =========================
# 5) KPIs (usando df_filtrado)
# =========================
total_users = df_filtrado["user_id"].nunique()
premium_pct = (df_filtrado["subscription_type"].astype(str).str.lower() != "free").mean() * 100
inactive_pct = df_filtrado["inactive_3_months_flag"].mean() * 100 if df_filtrado["inactive_3_months_flag"].notna().any() else 0

avg_hours = df_filtrado["avg_listening_hours_per_week"].mean()
avg_skips = df_filtrado["avg_skips_per_day"].mean()
avg_rating = df_filtrado["music_suggestion_rating_1_to_5"].mean()

# Correção aqui: checagem usando df_filtrado
interagiram = df_filtrado["ad_interaction"].sum() if df_filtrado["ad_interaction"].notna().any() else 0
converteram = df_filtrado["ad_conversion_to_subscription"].sum() if df_filtrado["ad_conversion_to_subscription"].notna().any() else 0
ad_conv_rate = (converteram / interagiram * 100) if interagiram else 0

# Exibir KPIs
c1, c2, c3, c4, c5, c6 = st.columns(6)
c1.metric("👥 Usuários", f"{total_users:,}".replace(",", "."))
c2.metric("💳 Premium (%)", f"{premium_pct:.1f}%")
c3.metric("📉 Inativos 3m (%)", f"{inactive_pct:.1f}%")
c4.metric("🎧 Horas/sem (média)", f"{avg_hours:.2f}")
c5.metric("⏭️ Skips/dia (média)", f"{avg_skips:.2f}")
c6.metric("📢 Conv. Anúncio (%)", f"{ad_conv_rate:.1f}%")

# Graficos de distribuição de assinaturas
st.divider()
col1, col2 = st.columns(2)
with col1:
    st.subheader("📊 Quantidade de Usuários por Assinatura")
    graph_bar_assinaturas = df["subscription_type"].value_counts()
    st.bar_chart(graph_bar_assinaturas)

with col2:
    st.subheader("📊 Distribuição Percentual de Assinaturas")
    graph_pie_assinatura = df["subscription_type"].value_counts().reset_index()
    graph_pie_assinatura.columns = ["Tipo de Assinatura", "Quantidade"]

    fig = px.pie(
    graph_pie_assinatura,
    names="Tipo de Assinatura",
    values="Quantidade"
    )

    fig.update_layout(
    font=dict(size=16)
    )

    st.plotly_chart(fig, use_container_width=True)

# Graficos de distribuição de assinaturas
st.divider()

# ✅ GRÁFICO DE PAÍS
st.subheader("🌍 Quantidade de usuários por país")

qtd_paises = df_filtrado["country"].dropna().nunique()

min_slider = 1 if qtd_paises < 5 else 5
max_slider = max(1, qtd_paises)
valor_padrao = min(15, max_slider)

n_exibir = st.slider(
    "Quantidade de países exibidos",
    min_value=min_slider,
    max_value=max_slider,
    value=valor_padrao
)

usuarios_por_pais = (
    df_filtrado.groupby("country")["user_id"]
    .nunique()
    .sort_values(ascending=False)
    .head(n_exibir)
)

st.bar_chart(usuarios_por_pais)

st.caption("Mostra usuários únicos por país (respeita o filtro de assinatura).")

st.divider()

# ✅ HEATMAP: Conversão de anúncios por dispositivo
st.subheader("🔥 Conversão de anúncios por dispositivo (%)")

df_temp = df_filtrado.copy()

conversao_por_device = (
    df_temp.groupby("primary_device")
    .agg(
        interacoes=("ad_interaction", "sum"),
        conversoes=("ad_conversion_to_subscription", "sum")
    )
)

# 👉 cálculo da taxa em % + arredondamento
conversao_por_device["taxa_conversao"] = (
    conversao_por_device["conversoes"]
    / conversao_por_device["interacoes"]
    * 100
).round(2)

# 👉 evita erros
conversao_por_device = (
    conversao_por_device
    .replace([float("inf"), -float("inf")], 0)
    .fillna(0)
)

# 👉 criação do heatmap
fig = px.imshow(
    [conversao_por_device["taxa_conversao"].values],
    labels=dict(x="Dispositivo", color="Taxa (%)"),
    x=conversao_por_device.index,
    text_auto=True,
    aspect="auto"
)

st.plotly_chart(fig, use_container_width=True)

st.caption("Taxa de conversão de anúncios (%) por dispositivo.")


st.subheader("📊 Distribuição por Idade")
grafico_idade = df_filtrado.groupby("age")["avg_listening_hours_per_week"].mean()
st.bar_chart(grafico_idade)

st.caption("✅ KPIs prontos.")
