# ---------------------------------------------------------
# 3_Summary.py — Zweisprachige Version (DE/EN)
# ---------------------------------------------------------

import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
from utils import t   # Übersetzungsfunktion

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(
    page_title= t("home_title"),
    layout="wide"
)

st.markdown("""
    <style>
        .sidebar-divider {
            height: 2px;
            background-color: #cccccc;
            margin: 15px 0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    /* Alle Präsentationsseiten aus der Sidebar entfernen */
    section[data-testid="stSidebarNav"] li a[href*="presentation_"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>

div[data-baseweb="select"] > div {
    background-color: #1E2A5A !important;   /* dunkler Hintergrund */
    color: white !important;                /* weiße Schrift */
    border: 1px solid white !important;
}

div[data-baseweb="select"] svg {
    fill: white !important;                 /* weißer Pfeil */
}

div[data-baseweb="popover"] {
    background-color: #1E2A5A !important;   /* Dropdown-Liste dunkel */
    color: white !important;
}

div[data-baseweb="option"] {
    background-color: #1E2A5A !important;
    color: white !important;
}

div[data-baseweb="option"]:hover {
    background-color: #2F3B6F !important;   /* Hover-Farbe */
    color: #FFD700 !important;              /* Gold */
}

</style>
""", unsafe_allow_html=True)


st.session_state["presentation_mode"] = False

#Sidebar trennen
st.sidebar.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar: Logout
# ---------------------------------------------------------
with st.sidebar:
    #st.header(t("nav_header"))
    st.success(f"{t('logged_in_as')} {st.session_state['username']}")

    if st.button(t("logout")):
        st.session_state.clear()
        st.switch_page("pages/login.py")

#Sidebar trennen
st.sidebar.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)


#Sprache Dropdown
with st.sidebar:
    st.markdown("<h3 style='color:white;'>🌐 Sprache / Language</h3>", unsafe_allow_html=True)

    language_display = {
        "de": "🇩🇪 Deutsch",
        "en": "🇬🇧 English"
    }

    selected_language = st.selectbox(
        "",
        options=["de", "en"],
        format_func=lambda x: language_display[x],
        index=0 if st.session_state.get("lang", "de") == "de" else 1,
        key="lang_selector"
    )

    st.session_state["lang"] = selected_language

# ---------------------------------------------------------
# Zugriffsschutz
# ---------------------------------------------------------
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning(t("login_required"))
    st.switch_page("pages/login.py")
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
        host="db.xxdveopyipxzclzmhfde.supabase.co",
        database="postgres",
        user="postgres",
        password="Gael2012!&237",
        port=5432,
        sslmode="require"
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

#Sidebar trennen
st.sidebar.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)


# ---------------------------------------------------------
# Filter
# ---------------------------------------------------------
st.sidebar.header(t("filter_header"))

year_options = [t("all_option")] + sorted(df["year"].unique().tolist())
selected_years = st.sidebar.multiselect(t("filter_years"), year_options, default=t("all_option"))
years = df["year"].unique() if t("all_option") in selected_years or not selected_years else selected_years

country_options = [t("all_option")] + sorted(df["country_name"].unique().tolist())
selected_countries = st.sidebar.multiselect(t("filter_countries"), country_options, default=t("all_option"))
countries = df["country_name"].unique() if t("all_option") in selected_countries or not selected_countries else selected_countries

product_options = [t("all_option")] + sorted(df["product_name"].unique().tolist())
selected_products = st.sidebar.multiselect(t("filter_products"), product_options, default=t("all_option"))
products = df["product_name"].unique() if t("all_option") in selected_products or not selected_products else selected_products



filtered = df[
    df["year"].isin(years) &
    df["product_name"].isin(products) &
    df["country_name"].isin(countries)
]

#st.subheader(t("summary_overview_title"))




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
    
    fig_top_products.for_each_xaxis(lambda axis: axis.update(title_text="", showticklabels=False))

    #fig_top_products.update_xaxes(showticklabels=False)
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
    filtered.groupby("year")["price"]
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
# CSV-Download
# ---------------------------------------------------------
st.subheader(t("download_title"))

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label=t("download_csv"),
    data=csv,
    file_name="import_data_filtered.csv",
    mime="text/csv"
)

# ---------------------------------------------------------
# Detailtabelle
# ---------------------------------------------------------
st.subheader(t("detail_table"))
st.dataframe(filtered.sort_values(["year", "country_name", "product_name"]))



st.markdown("""
<style>

/* Sticky Fußzeile – dunkelblau für alle Seiten */
.footer-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 55px;
    background: linear-gradient(90deg, #001a33, #003366); /* dunkles Blau */
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: 500;
    letter-spacing: 0.6px;
    z-index: 9999;
    animation: footerFadeIn 1.2s ease-out;
}

/* Einblend-Animation */
@keyframes footerFadeIn {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}

/* Abstand unten, damit Footer nichts überlappt */
.slide-content, .main > div {
    padding-bottom: 120px !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    f"<div class='footer-bar'>{t('footer_project_info')}</div>",
    unsafe_allow_html=True
)