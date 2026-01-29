import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

# ---------------------------------------------------------
# Sidebar Styling
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
# DB Verbindung
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
# Layout
# ---------------------------------------------------------
st.set_page_config(page_title="Summary Dashboard", layout="wide")
st.title("📘 Zusammenfassung – Kritische Rohstoffe")

df = load_data()

# ---------------------------------------------------------
# Sidebar Filter
# ---------------------------------------------------------
st.sidebar.header("Filter")

# Jahr
year_options = ["Alle"] + sorted(df["year"].unique().tolist())
selected_year = st.sidebar.selectbox("Jahr auswählen", year_options, index=0)

# Produkt
product_options = ["Alle"] + sorted(df["product_name"].unique().tolist())
selected_product = st.sidebar.selectbox("Produkt auswählen", product_options, index=0)

# Land
country_options = ["Alle"] + sorted(df["country_name"].unique().tolist())
selected_country = st.sidebar.selectbox("Land auswählen", country_options, index=0)

# Filter anwenden
filtered = df.copy()

if selected_year != "Alle":
    filtered = filtered[filtered["year"] == selected_year]

if selected_product != "Alle":
    filtered = filtered[filtered["product_name"] == selected_product]

if selected_country != "Alle":
    filtered = filtered[filtered["country_name"] == selected_country]

# ---------------------------------------------------------
# Top 5 Länder je Produkt
# ---------------------------------------------------------
st.subheader("🌍 Top 5 Länder je Produkt")

top_countries = (
    df.groupby(["product_name", "country_name"])["price"]
    .sum()
    .reset_index()
    .sort_values(["product_name", "price"], ascending=[True, False])
)

if selected_product != "Alle":
    top_countries = top_countries[top_countries["product_name"] == selected_product]

top5 = top_countries.groupby("product_name").head(5)

fig_top_countries = px.bar(
    top5,
    x="country_name",
    y="price",
    color="country_name",
    facet_col="product_name",
    title="Top 5 Länder je Produkt",
)
st.plotly_chart(fig_top_countries, use_container_width=True)

# ---------------------------------------------------------
# Top 5 Produkte pro Jahr
# ---------------------------------------------------------
st.subheader("📦 Top 5 Produkte pro Jahr")

top_products = (
    df.groupby(["year", "product_name"])["price"]
    .sum()
    .reset_index()
    .sort_values(["year", "price"], ascending=[True, False])
)

if selected_year != "Alle":
    top_products = top_products[top_products["year"] == selected_year]

top5_products = top_products.groupby("year").head(5)

fig_top_products = px.bar(
    top5_products,
    x="product_name",
    y="price",
    color="product_name",
    facet_col="year",
    title="Top 5 Produkte pro Jahr",
)
st.plotly_chart(fig_top_products, use_container_width=True)

# ---------------------------------------------------------
# Automatische Insights
# ---------------------------------------------------------
st.subheader("🧠 Automatische Insights")

insights = []

# Insight 1: Dominantestes Land
dom_land = (
    filtered.groupby("country_name")["price"]
    .sum()
    .sort_values(ascending=False)
)

if len(dom_land) > 0:
    land = dom_land.index[0]
    share = dom_land.iloc[0] / dom_land.sum() * 100
    insights.append(f"• **{land}** ist das wichtigste Lieferland mit **{share:.1f}%** Anteil.")

# Insight 2: Dominantestes Produkt
dom_prod = (
    filtered.groupby("product_name")["price"]
    .sum()
    .sort_values(ascending=False)
)

if len(dom_prod) > 0:
    prod = dom_prod.index[0]
    share = dom_prod.iloc[0] / dom_prod.sum() * 100
    insights.append(f"• Das Produkt **{prod}** dominiert die Importe mit **{share:.1f}%** Anteil.")

# Insight 3: Risiko
if len(dom_land) > 0:
    if share > 50:
        insights.append("• ⚠️ Die Importabhängigkeit ist **kritisch hoch** (über 50%).")
    else:
        insights.append("• Die Importabhängigkeit ist **moderat**.")

# Insight 4: Trend
trend = (
    df.groupby("year")["price"]
    .sum()
    .pct_change()
    .iloc[-1]
)

if pd.notnull(trend):
    if trend > 0:
        insights.append(f"• Die Importe steigen aktuell um **{trend*100:.1f}%**.")
    else:
        insights.append(f"• Die Importe sinken aktuell um **{abs(trend*100):.1f}%**.")

# Ausgabe
for i in insights:
    st.markdown(i)

# ---------------------------------------------------------
# Detailtabelle
# ---------------------------------------------------------
st.subheader("Detailtabelle")
st.dataframe(filtered.sort_values(["year", "country_name", "product_name"]))