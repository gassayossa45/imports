import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

# ---------------------------------------------------------
# Sidebar Styling (dunkelblau)
# ---------------------------------------------------------
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #0A1A44;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# PostgreSQL Verbindung
# ---------------------------------------------------------
def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="imports",
        user="postgres",
        password="gassa"
    )

@st.cache_data
def load_data():
    conn = get_connection()
    query = """
        SELECT
            f.import_id,
            dy.year,
            dc.country_name,
            dp.hs_code,
            dp.product_name,
            f.quantity,
            f.netweight,
            f.price
        FROM fact_imports f
        JOIN dim_years dy ON f.year_id = dy.year_id
        JOIN dim_countries dc ON f.country_id = dc.country_id
        JOIN dim_products dp ON f.hs_code = dp.hs_code;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# ---------------------------------------------------------
# Streamlit Layout
# ---------------------------------------------------------
st.set_page_config(page_title="Risikoanalyse – Kritische Rohstoffe", layout="wide")
st.title("⚠️ Risikoanalyse kritischer Rohstoffe")

df = load_data()

# ---------------------------------------------------------
# Sidebar Filter mit „Alle auswählen“
# ---------------------------------------------------------
st.sidebar.header("Filter")

# Jahre
year_options = ["Alle"] + sorted(df["year"].unique().tolist())
selected_years = st.sidebar.multiselect("Jahre auswählen", year_options, default="Alle")
years = df["year"].unique() if "Alle" in selected_years else selected_years

# Länder
country_options = ["Alle"] + sorted(df["country_name"].unique().tolist())
selected_countries = st.sidebar.multiselect("Länder auswählen", country_options, default="Alle")
countries = df["country_name"].unique() if "Alle" in selected_countries else selected_countries

# Produkte
product_options = ["Alle"] + sorted(df["product_name"].unique().tolist())
selected_products = st.sidebar.multiselect("Produkte auswählen", product_options, default="Alle")
products = df["product_name"].unique() if "Alle" in selected_products else selected_products

# Gefilterte Daten
filtered = df[
    df["year"].isin(years) &
    df["country_name"].isin(countries) &
    df["product_name"].isin(products)
]

# ---------------------------------------------------------
# Risiko-Heatmap
# ---------------------------------------------------------
st.subheader("🔥 Risiko-Heatmap: Importabhängigkeit")

risk = filtered.groupby(["country_name", "product_name"], as_index=False)["price"].sum()
total = risk["price"].sum()
risk["dependency"] = risk["price"] / total

heatmap_df = risk.pivot(index="country_name", columns="product_name", values="dependency")

fig_heat = px.imshow(
    heatmap_df,
    color_continuous_scale="Reds",
    aspect="auto",
    labels=dict(color="Abhängigkeit"),
)
st.plotly_chart(fig_heat, use_container_width=True)

# ---------------------------------------------------------
# HHI-Index (Konzentrationsrisiko)
# ---------------------------------------------------------
st.subheader("📉 HHI-Konzentrationsindex (Lieferländer)")

hhi = (
    filtered.groupby("country_name")["price"].sum() /
    filtered["price"].sum()
) ** 2

hhi_value = hhi.sum()

st.metric("HHI-Index", f"{hhi_value:.3f}")

# ---------------------------------------------------------
# China Exposure
# ---------------------------------------------------------
st.subheader("🇨🇳 China Exposure pro Produkt")

china_df = filtered[filtered["country_name"] == "China"]
china_exposure = (
    china_df.groupby("product_name")["price"].sum() /
    filtered.groupby("product_name")["price"].sum()
).reset_index(name="china_share")

fig_china = px.bar(
    china_exposure,
    x="product_name",
    y="china_share",
    title="China-Anteil am Importwert pro Produkt",
    labels={"china_share": "China-Anteil", "product_name": "Produkt"},
)
fig_china.update_xaxes(tickangle=45)
st.plotly_chart(fig_china, use_container_width=True)

# ---------------------------------------------------------
# Risiko-Trend über die Jahre
# ---------------------------------------------------------
st.subheader("📈 Risiko-Trend: Konzentration über die Jahre")

trend = (
    df.groupby(["year", "country_name"])["price"].sum()
    .groupby(level=0)
    .apply(lambda x: ((x / x.sum()) ** 2).sum())
    .reset_index(name="hhi")
)

fig_trend = px.line(
    trend,
    x="year",
    y="hhi",
    markers=True,
    title="HHI-Konzentrationsindex über die Jahre",
    labels={"hhi": "HHI", "year": "Jahr"},
)
st.plotly_chart(fig_trend, use_container_width=True)

# ---------------------------------------------------------
# Detailtabelle
# ---------------------------------------------------------
st.subheader("Detailtabelle")
st.dataframe(filtered.sort_values(["year", "country_name", "product_name"]))