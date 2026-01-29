import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

#3_Summary.py

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

# Zugriffsschutz
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("Bitte zuerst einloggen.")
    st.switch_page("pages/login.py")
    st.stop()


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

st.title("📘 Summary – Top 5 & Insights")

df = load_data()

# Filter wie in den anderen Dashboards
st.sidebar.header("Filter")

year_options = ["Alle"] + sorted(df["year"].unique().tolist())
selected_years = st.sidebar.multiselect("Jahre auswählen", year_options, default="Alle")
years = df["year"].unique() if "Alle" in selected_years or not selected_years else selected_years

product_options = ["Alle"] + sorted(df["product_name"].unique().tolist())
selected_products = st.sidebar.multiselect("Produkte auswählen", product_options, default="Alle")
products = df["product_name"].unique() if "Alle" in selected_products or not selected_products else selected_products

country_options = ["Alle"] + sorted(df["country_name"].unique().tolist())
selected_countries = st.sidebar.multiselect("Länder auswählen", country_options, default="Alle")
countries = df["country_name"].unique() if "Alle" in selected_countries or not selected_countries else selected_countries

filtered = df[
    df["year"].isin(years) &
    df["product_name"].isin(products) &
    df["country_name"].isin(countries)
]

# Top 5 Länder je Produkt
st.subheader("🌍 Top 5 Länder je Produkt")

top_countries = (
    df.groupby(["product_name", "country_name"])["price"]
    .sum()
    .reset_index()
    .sort_values(["product_name", "price"], ascending=[True, False])
)

if len(products) != len(df["product_name"].unique()):
    top_countries = top_countries[top_countries["product_name"].isin(products)]

top5_countries = top_countries.groupby("product_name").head(5)

if not top5_countries.empty:
    fig_top_countries = px.bar(
        top5_countries,
        x="country_name",
        y="price",
        color="country_name",
       #facet_col="product_name",
       #title="Top 5 Länder je Produkt",
    )
    st.plotly_chart(fig_top_countries, use_container_width=True)
else:
    st.info("Keine Daten für Top-5 Länder je Produkt.")

# Top 5 Produkte pro Jahr
st.subheader("📦 Top 5 Produkte pro Jahr")

top_products = (
    df.groupby(["year", "product_name"])["price"]
    .sum()
    .reset_index()
    .sort_values(["year", "price"], ascending=[True, False])
)

if len(years) != len(df["year"].unique()):
    top_products = top_products[top_products["year"].isin(years)]

top5_products = top_products.groupby("year").head(5)

if not top5_products.empty:
    fig_top_products = px.bar(
        top5_products,
        x="product_name",
        y="price",
        color="product_name",
        facet_col="year",
        #title="Top 5 Produkte pro Jahr",
    )
    fig_top_products.update_xaxes(tickangle=45)
    st.plotly_chart(fig_top_products, use_container_width=True)
else:
    st.info("Keine Daten für Top-5 Produkte pro Jahr.")

# Automatische Insights
st.subheader("🧠 Automatische Insights")

insights = []

dom_land = (
    filtered.groupby("country_name")["price"]
    .sum()
    .sort_values(ascending=False)
)

if len(dom_land) > 0:
    land = dom_land.index[0]
    share_land = dom_land.iloc[0] / dom_land.sum() * 100
    insights.append(f"• **{land}** ist aktuell das wichtigste Lieferland mit **{share_land:.1f}%** Anteil am Importwert.")

dom_prod = (
    filtered.groupby("product_name")["price"]
    .sum()
    .sort_values(ascending=False)
)

if len(dom_prod) > 0:
    prod = dom_prod.index[0]
    share_prod = dom_prod.iloc[0] / dom_prod.sum() * 100
    insights.append(f"• Das Produkt **{prod}** dominiert die Importe mit **{share_prod:.1f}%** Anteil.")

if len(dom_land) > 0 and share_land > 50:
    insights.append("• ⚠️ Die Importabhängigkeit von einem einzelnen Land ist **kritisch hoch** (über 50%).")

trend = (
    df.groupby("year")["price"]
    .sum()
    .pct_change()
    .iloc[-1]
)

if pd.notnull(trend):
    if trend > 0:
        insights.append(f"• Die Importe steigen aktuell um **{trend*100:.1f}%** gegenüber dem Vorjahr.")
    else:
        insights.append(f"• Die Importe sinken aktuell um **{abs(trend*100):.1f}%** gegenüber dem Vorjahr.")

if insights:
    for i in insights:
        st.markdown(i)
else:
    st.info("Keine aussagekräftigen Insights für die aktuelle Filterauswahl.")

st.subheader("Detailtabelle")
st.dataframe(filtered.sort_values(["year", "country_name", "product_name"]))

with st.sidebar:
    st.header("Navigation")
    st.success(f"Angemeldet als {st.session_state['username']}")
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.switch_page("pages/login.py")