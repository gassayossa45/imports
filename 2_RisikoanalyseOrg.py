import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

#2_Risikoanalyse.py

# Zugriffsschutz
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("Bitte zuerst einloggen.")
    st.switch_page("pages/login.py")
    st.stop()

st.markdown("""
    <style>
        /* Sidebar Hintergrund */
        [data-testid="stSidebar"] {
            background-color: #0A1A44;
        }

        /* Sidebar Schriftfarbe */
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Sidebar Buttons */
        [data-testid="stSidebar"] button {
            background-color: #1E2A5A !important;
            color: white !important;
            border: 1px solid white !important;
        }

        /* Sidebar Button Hover */
        [data-testid="stSidebar"] button:hover {
            background-color: #2F3B6F !important;
            color: #FFD700 !important;
            border: 1px solid #FFD700 !important;
        }

        /* Sidebar Header */
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)
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

st.title("⚠️ Risikoanalyse kritischer Rohstoffe")

df = load_data()

st.sidebar.header("Filter")

year_options = ["Alle"] + sorted(df["year"].unique().tolist())
selected_years = st.sidebar.multiselect("Jahre auswählen", year_options, default="Alle")
years = df["year"].unique() if "Alle" in selected_years or not selected_years else selected_years

country_options = ["Alle"] + sorted(df["country_name"].unique().tolist())
selected_countries = st.sidebar.multiselect("Länder auswählen", country_options, default="Alle")
countries = df["country_name"].unique() if "Alle" in selected_countries or not selected_countries else selected_countries

product_options = ["Alle"] + sorted(df["product_name"].unique().tolist())
selected_products = st.sidebar.multiselect("Produkte auswählen", product_options, default="Alle")
products = df["product_name"].unique() if "Alle" in selected_products or not selected_products else selected_products

filtered = df[
    df["year"].isin(years) &
    df["country_name"].isin(countries) &
    df["product_name"].isin(products)
]

# Risiko-Heatmap
st.subheader("🔥 Risiko-Heatmap: Importabhängigkeit")
if not filtered.empty:
    risk = filtered.groupby(["country_name", "product_name"], as_index=False)["price"].sum()
    total_risk = risk["price"].sum()
    risk["dependency"] = risk["price"] / total_risk if total_risk > 0 else 0
    heatmap_df = risk.pivot(index="country_name", columns="product_name", values="dependency")
    fig_heat = px.imshow(heatmap_df, color_continuous_scale="Reds", aspect="auto")
    st.plotly_chart(fig_heat, use_container_width=True)
else:
    st.info("Keine Daten für die aktuelle Filterauswahl.")

# HHI
st.subheader("📉 HHI-Konzentrationsindex (Lieferländer)")
if not filtered.empty:
    shares = filtered.groupby("country_name")["price"].sum() / filtered["price"].sum()
    hhi_value = (shares ** 2).sum()
    st.metric("HHI-Index", f"{hhi_value:.3f}")
else:
    st.info("Keine Daten für HHI-Berechnung.")

# China Exposure
st.subheader("🇨🇳 China Exposure pro Produkt")
if not filtered.empty:
    china_df = filtered[filtered["country_name"] == "China"]
    if not china_df.empty:
        china_exposure = (
            china_df.groupby("product_name")["price"].sum() /
            filtered.groupby("product_name")["price"].sum()
        ).reset_index(name="china_share")
        fig_china = px.bar(china_exposure, x="product_name", y="china_share")
        fig_china.update_xaxes(tickangle=45)
        st.plotly_chart(fig_china, use_container_width=True)
    else:
        st.info("Keine China-Importe in der aktuellen Filterauswahl.")
else:
    st.info("Keine Daten für China-Exposure.")

# HHI-Trend
st.subheader("📈 Risiko-Trend: HHI über die Jahre")
trend = (
    df.groupby(["year", "country_name"])["price"].sum()
    .groupby(level=0)
    .apply(lambda x: ((x / x.sum()) ** 2).sum())
    .reset_index(name="hhi")
)
fig_trend = px.line(trend, x="year", y="hhi", markers=True)
st.plotly_chart(fig_trend, use_container_width=True)

st.subheader("Detailtabelle")
st.dataframe(filtered.sort_values(["year", "country_name", "product_name"]))

with st.sidebar:
    st.header("Navigation")
    st.success(f"Angemeldet als {st.session_state['username']}")
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.switch_page("pages/login.py")