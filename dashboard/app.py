import streamlit as st
import pandas as pd

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

# Garantir que a flag é booleana (caso venha 0/1 ou texto)
df["inactive_3_months_flag"] = df["inactive_3_months_flag"].astype(str).str.lower().map(
    {"1": True, "0": False, "true": True, "false": False}
)

# Anúncios (podem estar como 0/1)
for c in ["ad_interaction", "ad_conversion_to_subscription"]:
    df[c] = df[c].astype(str).str.lower().map({"1": True, "0": False, "true": True, "false": False})

# Numéricos
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

st.sidebar.header("🔍Filtrar Assinaturas")

opcoes_assinaturas = ["Todos"] + list (df["subscription_type"].unique())
filtro_assinatura = st.sidebar.selectbox("Tipo de Assinatura", opcoes_assinaturas)

# =========================
# 4) Aplicação dos Filtros (Efeito Cascata)
# =========================

if filtro_assinatura == "Todos":
    df_filtrado = df
else:
    df_filtrado = df[df["subscription_type"] == filtro_assinatura]

# =========================
# 5) KPIs (Agora usando o df_filtrado)
# =========================

total_users = df_filtrado["user_id"].nunique()

premium_pct = (df_filtrado["subscription_type"].astype(str).str.lower() != "free").mean() * 100

inactive_pct = df_filtrado["inactive_3_months_flag"].mean() * 100 if df_filtrado["inactive_3_months_flag"].notna().any() else 0

avg_hours = df_filtrado["avg_listening_hours_per_week"].mean()
avg_skips = df_filtrado["avg_skips_per_day"].mean()
avg_rating = df_filtrado["music_suggestion_rating_1_to_5"].mean()

# Conversão de anúncios (entre quem interagiu, quantos converteram)
interagiram = df_filtrado["ad_interaction"].sum() if df["ad_interaction"].notna().any() else 0
converteram = df_filtrado["ad_conversion_to_subscription"].sum() if df["ad_conversion_to_subscription"].notna().any() else 0
ad_conv_rate = (converteram / interagiram * 100) if interagiram else 0


# Exibir KPIs
c1, c2, c3, c4, c5, c6 = st.columns(6)
c1.metric("👥 Usuários", f"{total_users:,}".replace(",", "."))
c2.metric("💳 Premium (%)", f"{premium_pct:.1f}%")
c3.metric("📉 Inativos 3m (%)", f"{inactive_pct:.1f}%")
c4.metric("🎧 Horas/sem (média)", f"{avg_hours:.2f}")
c5.metric("⏭️ Skips/dia (média)", f"{avg_skips:.2f}")
c6.metric("📢 Conv. Anúncio (%)", f"{ad_conv_rate:.1f}%")

st.divider()
st.subheader("📊Distribuição por Idade")
grafico_idade = df_filtrado.groupby("age")["avg_listening_hours_per_week"].mean()
st.bar_chart(grafico_idade)

st.caption("✅ KPIs prontos.")
