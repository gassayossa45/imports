# ---------------------------------------------------------
# 3_Summary.py — Zweisprachige Version (DE/EN)
# ---------------------------------------------------------

import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
from utils import t   # Übersetzungsfunktion

# ---------------------------------------------------------
# Zugriffsschutz
# ---------------------------------------------------------
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning(t("login_required"))
    st.switch_page("login.py")
    st.stop()

# ---------------------------------------------------------
# Styling (unverändert)
# ---------------------------------------------------------
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #0A1A44;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }
        [data-testid="stSidebar"] button {
            background-color: #1E2A5A !important;
            color: white !important;
            border: 1px solid white !important;
        }
        [data-testid="stSidebar"] button:hover {
            background-color: #2F3B6F !important;
            color: #FFD700 !important;
            border: 1px solid #FFD700 !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# DB-Verbindung
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
# Titel
# ---------------------------------------------------------
st.title(t("summary_title"))

df = load_data()

# ---------------------------------------------------------
# Filter
# ---------------------------------------------------------
st.sidebar.header(t("filter_header"))

year_options = [t("all_option")] + sorted(df["year"].unique().tolist())
selected_years = st.sidebar.multiselect(t("filter_years"), year_options, default=t("all_option"))
years = df["year"].unique() if t("all_option") in selected_years or not selected_years else selected_years

product_options = [t("all_option")] + sorted(df["product_name"].unique().tolist())
selected_products = st.sidebar.multiselect(t("filter_products"), product_options, default=t("all_option"))
products = df["product_name"].unique() if t("all_option") in selected_products or not selected_products else selected_products

country_options = [t("all_option")] + sorted(df["country_name"].unique().tolist())
selected_countries = st.sidebar.multiselect(t("filter_countries"), country_options, default=t("all_option"))
countries = df["country_name"].unique() if t("all_option") in selected_countries or not selected_countries else selected_countries

filtered = df[
    df["year"].isin(years) &
    df["product_name"].isin(products) &
    df["country_name"].isin(countries)
]

# ---------------------------------------------------------
# Top 5 Länder je Produkt
# ---------------------------------------------------------
st.subheader(t("top5_countries_title"))

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
        color="country_name"
    )
    st.plotly_chart(fig_top_countries, use_container_width=True)
else:
    st.info(t("no_top5_countries"))

# ---------------------------------------------------------
# Top 5 Produkte pro Jahr
# ---------------------------------------------------------
st.subheader(t("top5_products_title"))

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
        facet_col="year"
    )
    fig_top_products.update_xaxes(tickangle=45)
    st.plotly_chart(fig_top_products, use_container_width=True)
else:
    st.info(t("no_top5_products"))

# ---------------------------------------------------------
# Automatische Insights
# ---------------------------------------------------------
st.subheader(t("insights_title"))

insights = []

# Wichtigstes Lieferland
dom_land = (
    filtered.groupby("country_name")["price"]
    .sum()
    .sort_values(ascending=False)
)

if len(dom_land) > 0:
    land = dom_land.index[0]
    share_land = dom_land.iloc[0] / dom_land.sum() * 100
    insights.append(t("insight_top_country").format(land=land, share=share_land))

# Wichtigstes Produkt
dom_prod = (
    filtered.groupby("product_name")["price"]
    .sum()
    .sort_values(ascending=False)
)

if len(dom_prod) > 0:
    prod = dom_prod.index[0]
    share_prod = dom_prod.iloc[0] / dom_prod.sum() * 100
    insights.append(t("insight_top_product").format(prod=prod, share=share_prod))

# Kritische Abhängigkeit
if len(dom_land) > 0 and share_land > 50:
    insights.append(t("insight_dependency_high"))

# Trend
trend = (
    df.groupby("year")["price"]
    .sum()
    .pct_change()
    .iloc[-1]
)

if pd.notnull(trend):
    if trend > 0:
        insights.append(t("insight_trend_up").format(pct=trend * 100))
    else:
        insights.append(t("insight_trend_down").format(pct=abs(trend * 100)))

# Ausgabe
if insights:
    for i in insights:
        st.markdown(i)
else:
    st.info(t("no_insights"))

# ---------------------------------------------------------
# Detailtabelle
# ---------------------------------------------------------
st.subheader(t("detail_table"))
st.dataframe(filtered.sort_values(["year", "country_name", "product_name"]))

# ---------------------------------------------------------
# Sidebar Logout
# ---------------------------------------------------------
with st.sidebar:
    st.header(t("nav_header"))
    st.success(f"{t('logged_in_as')} {st.session_state['username']}")

    if st.button(t("logout")):
        st.session_state.clear()
        st.switch_page("login.py")