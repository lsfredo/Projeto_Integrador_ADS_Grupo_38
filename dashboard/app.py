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
c3.metric("📉 Inativos por 3 meses (%)", f"{inactive_pct:.1f}%")
c4.metric("🎧 Horas semanais (média)", f"{avg_hours:.2f}")
c5.metric("⏭️ Skips/dia (média)", f"{avg_skips:.2f}")
c6.metric("📢 Taxa de conversão de anúncios (%)", f"{ad_conv_rate:.1f}%")

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


# ✅ Análise temporal de cadastros
st.subheader("📈 Evolução de novos usuários ao longo do tempo")

df_temp = df_filtrado.copy()

# Criar período mensal (ano-mês)
df_temp["signup_periodo"] = df_temp["signup_date"].dt.to_period("M").astype(str)

# Contagem de usuários por período (ordenado cronologicamente)
evolucao = (
    df_temp["signup_periodo"]
    .value_counts()
    .sort_index()
)

# Gráfico de linha
st.line_chart(evolucao)

st.caption("Quantidade de novos usuários por mês.")

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

st.divider()

# ✅ Barras empilhadas: Gêneros favoritos por plano
st.subheader("🎵 Gêneros favoritos por plano (barras empilhadas)")

# Cópia para evitar modificar df_filtrado
df_temp = df_filtrado.copy()

# (Opcional) Limitar quantidade de gêneros exibidos para ficar legível
top_n_generos = st.slider("Top N gêneros exibidos", min_value=5, max_value=20, value=10)

top_generos = (
    df_temp["favorite_genre"]
    .value_counts()
    .head(top_n_generos)
    .index
)

df_temp["favorite_genre_plot"] = df_temp["favorite_genre"].where(
    df_temp["favorite_genre"].isin(top_generos),
    other="Outros"
)

# Tabela de contagem: plano x gênero
tabela = (
    df_temp.groupby(["subscription_type", "favorite_genre_plot"])
    .size()
    .reset_index(name="qtd")
)

# Alternar entre contagem absoluta e percentual
modo = st.radio("Exibir como:", ["Contagem", "Percentual (%)"], horizontal=True)

if modo == "Percentual (%)":
    total_por_plano = tabela.groupby("subscription_type")["qtd"].transform("sum")
    tabela["valor"] = (tabela["qtd"] / total_por_plano * 100).round(2)
    y_label = "Percentual (%)"
else:
    tabela["valor"] = tabela["qtd"]
    y_label = "Quantidade"

# Gráfico empilhado com Plotly
fig = px.bar(
    tabela,
    x="subscription_type",
    y="valor",
    color="favorite_genre_plot",
    barmode="stack",
    labels={
        "subscription_type": "Plano",
        "valor": y_label,
        "favorite_genre_plot": "Gênero"
    },
    title="Distribuição de gêneros favoritos por tipo de assinatura"
)

fig.update_layout(
    legend_title_text="Gênero",
    xaxis_title="Plano",
    yaxis_title=y_label
)

st.plotly_chart(fig, use_container_width=True)

st.caption("Barras empilhadas mostrando a distribuição de gêneros favoritos por plano. O filtro de assinatura afeta a amostra exibida.")

st.caption("Obs.: ao filtrar um plano específico, o gráfico mostra apenas o plano selecionado.")

st.divider()

# ✅ Dispersão(Ploty)
st.subheader("📈 Dispersão: Skips/dia × Horas/semana")

# Seleciona colunas e remove nulos
df_scatter = df_filtrado[
    ["avg_skips_per_day", "avg_listening_hours_per_week", "subscription_type"]
].dropna()

# Controles em um expander para não poluir a tela
with st.expander("⚙️ Ajustes do gráfico (limites para melhorar a leitura)", expanded=False):
    max_skips = st.slider("Limite máximo de skips/dia", min_value=10, max_value=200, value=100, step=5)
    max_horas = st.slider("Limite máximo de horas/semana", min_value=5, max_value=120, value=60, step=5)

# Aplica limites (reduz outliers e melhora visual)
df_scatter = df_scatter[
    (df_scatter["avg_skips_per_day"] <= max_skips) &
    (df_scatter["avg_listening_hours_per_week"] <= max_horas)
]

# Gráfico de dispersão
fig = px.scatter(
    df_scatter,
    x="avg_skips_per_day",
    y="avg_listening_hours_per_week",
    color="subscription_type",
    opacity=0.35,
    labels={
        "avg_skips_per_day": "Skips por dia (média)",
        "avg_listening_hours_per_week": "Horas por semana (média)",
        "subscription_type": "Plano"
    },
    title="Skips/dia vs Horas/semana (por tipo de assinatura)"
)

# Pequenos ajustes de layout
fig.update_layout(
    legend_title_text="Plano",
    xaxis_title="Skips por dia (média)",
    yaxis_title="Horas por semana (média)"
)

st.plotly_chart(fig, use_container_width=True)

st.caption("Dispersão do comportamento de escuta: relação entre skips/dia e horas/semana (respeita o filtro de assinatura).")

st.divider()

# ✅ Funil de conversão de usuários
st.subheader("🎯 Funil de conversão de usuários")

df_temp = df_filtrado.copy()

# Totais por etapa
total = len(df_temp)
interagiram = df_temp["ad_interaction"].sum()
converteram = df_temp["ad_conversion_to_subscription"].sum()

# Garantir valores inteiros
interagiram = int(interagiram) if pd.notna(interagiram) else 0
converteram = int(converteram) if pd.notna(converteram) else 0

# Estrutura do funil
funil = pd.DataFrame({
    "Etapa": [
        "Total de usuários",
        "Interagiram com anúncio",
        "Converteram"
    ],
    "Quantidade": [total, interagiram, converteram]
})

# Gráfico
st.bar_chart(funil.set_index("Etapa"))

# Cálculo das taxas
if total > 0:
    taxa_interacao = (interagiram / total) * 100
    taxa_conversao = (converteram / interagiram) * 100 if interagiram else 0

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Taxa de interação", f"{taxa_interacao:.2f}%")

    with col2:
        st.metric("Taxa de conversão", f"{taxa_conversao:.2f}%")

st.caption("Jornada dos usuários até a conversão.")

st.divider()

# ✅ Ajusta gráfico de idade para faixas etárias (bins)
st.subheader("📊 Distribuição por Faixa Etária")

df_temp = df_filtrado.copy()

# Garantir que age é numérico (caso venha como string)
df_temp["age"] = pd.to_numeric(df_temp["age"], errors="coerce")

# Definição de faixas (bins) + rótulos
bins = [0, 17, 24, 34, 44, 54, 64, 120]
labels = ["0-17", "18-24", "25-34", "35-44", "45-54", "55-64", "65+"]

# Criar coluna de faixa etária
df_temp["faixa_etaria"] = pd.cut(df_temp["age"], bins=bins, labels=labels, right=True)

# Média de horas semanais por faixa etária
grafico_faixa = (
    df_temp.groupby("faixa_etaria")["avg_listening_hours_per_week"]
    .mean()
    .dropna()
)

st.bar_chart(grafico_faixa)

st.caption("✅ KPIs prontos.")
