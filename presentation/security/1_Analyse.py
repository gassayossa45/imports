# ---------------------------------------------------------
# 1_Analyse.py — 
# Zweisprachige Version (Deutsch / Englisch)
# Enthält:
# - Zugriffsschutz
# - Titel
# - Filter
# - KPIs
# ---------------------------------------------------------

import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
from utils import t   # Übersetzungsfunktion
import pycountry

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
# Zugriffsschutz (zweisprachig)
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
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            color: white !important;
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
# Titel (zweisprachig)
# ---------------------------------------------------------
st.title(t("analysis_title"))

df = load_data()

# ---------------------------------------------------------
# Sidebar Filter (zweisprachig)
# ---------------------------------------------------------
st.sidebar.header(t("filter_header"))

# Jahre
year_options = [t("all_option")] + sorted(df["year"].unique().tolist())
selected_years = st.sidebar.multiselect(t("filter_years"), year_options, default=t("all_option"))
years = df["year"].unique() if t("all_option") in selected_years or not selected_years else selected_years

# Länder
country_options = [t("all_option")] + sorted(df["country_name"].unique().tolist())
selected_countries = st.sidebar.multiselect(t("filter_countries"), country_options, default=t("all_option"))
countries = df["country_name"].unique() if t("all_option") in selected_countries or not selected_countries else selected_countries

# Produkte
product_options = [t("all_option")] + sorted(df["product_name"].unique().tolist())
selected_products = st.sidebar.multiselect(t("filter_products"), product_options, default=t("all_option"))
products = df["product_name"].unique() if t("all_option") in selected_products or not selected_products else selected_products

# Gefilterte Daten
filtered = df[
    df["year"].isin(years) &
    df["country_name"].isin(countries) &
    df["product_name"].isin(products)
]

# ---------------------------------------------------------
# KPIs (zweisprachig)
# ---------------------------------------------------------
total_value = filtered["price"].sum()
total_weight = filtered["netweight"].sum()
avg_price = filtered["price"].mean()
price_per_kg = (total_value / total_weight) if total_weight > 0 else None

prev_year = max(years) - 1 if len(years) > 0 else None
prev_df = filtered[filtered["year"] == prev_year]
prev_total_value = prev_df["price"].sum()
prev_total_weight = prev_df["netweight"].sum()
prev_ppk = (prev_total_value / prev_total_weight) if prev_total_weight > 0 else None

if price_per_kg and prev_ppk:
    kpi_color = "#B00020" if price_per_kg > prev_ppk else "#008000"
else:
    kpi_color = "#444444"

formatted_value = f"{total_value:,.0f}"
formatted_weight = f"{total_weight:,.0f}"
formatted_avg = f"{avg_price:,.0f}" if pd.notnull(avg_price) else "–"
formatted_ppk = f"{price_per_kg:,.2f}" if price_per_kg else "–"

col1, col2, col3, col4 = st.columns(4)

col1.markdown(
    f"""
    <div style="background-color:#1E3A5F; padding:16px; border-radius:10px; text-align:center;">
        <h4 style="color:white;">{t("kpi_total_value")}</h4>
        <h2 style="color:white;">{formatted_value}</h2>
    </div>
    """,
    unsafe_allow_html=True
)

col2.markdown(
    f"""
    <div style="background-color:#1E3A5F; padding:16px; border-radius:10px; text-align:center;">
        <h4 style="color:white;">{t("kpi_total_weight")}</h4>
        <h2 style="color:white;">{formatted_weight}</h2>
    </div>
    """,
    unsafe_allow_html=True
)

col3.markdown(
    f"""
    <div style="background-color:#1E3A5F; padding:16px; border-radius:10px; text-align:center;">
        <h4 style="color:white;">{t("kpi_avg_price")}</h4>
        <h2 style="color:white;">{formatted_avg}</h2>
    </div>
    """,
    unsafe_allow_html=True
)

col4.markdown(
    f"""
    <div style="background-color:{kpi_color}; padding:16px; border-radius:10px; text-align:center;">
        <h4 style="color:white;">{t("kpi_price_per_kg")}</h4>
        <h2 style="color:white;">{formatted_ppk}</h2>
    </div>
    """,
    unsafe_allow_html=True
)



st.markdown("---")

# ---------------------------------------------------------
# 1_Analyse.py — 
# Zweisprachige Version (Deutsch / Englisch)
# Enthält:
# - Charts (Länder, Produkte)
# - Zeitreihen
# - YoY-Analyse
# ---------------------------------------------------------

# ---------------------------------------------------------
# Charts: Importwert nach Ländern
# ---------------------------------------------------------
colA, colB = st.columns(2)

with colA:
    st.subheader(t("chart_value_by_country"))

    if not filtered.empty:
        by_country = filtered.groupby("country_name", as_index=False)["price"].sum()
        fig_country = px.bar(
            by_country,
            x="country_name",
            y="price",
            labels={"country_name": "", "price": "USD"}
        )
        st.plotly_chart(fig_country, use_container_width=True)
    else:
        st.info(t("no_data"))

# ---------------------------------------------------------
# Charts: Importwert nach Produkten
# ---------------------------------------------------------
with colB:
    st.subheader(t("chart_value_by_product"))

    if not filtered.empty:
        by_product = filtered.groupby("product_name", as_index=False)["price"].sum()
        fig_product = px.bar(
            by_product,
            x="product_name",
            y="price",
            labels={"product_name": "", "price": "USD"}
        )
        fig_product.update_xaxes(tickangle=45)
        st.plotly_chart(fig_product, use_container_width=True)
    else:
        st.info(t("no_data"))

# ---------------------------------------------------------
# Zeitreihe: Importwert pro Jahr
# ---------------------------------------------------------
st.subheader(t("chart_value_per_year"))

if not filtered.empty:
    by_year = filtered.groupby("year", as_index=False)["price"].sum()
    fig_year = px.line(
        by_year,
        x="year",
        y="price",
        markers=True,
        labels={"year": "", "price": "USD"}
    )
    st.plotly_chart(fig_year, use_container_width=True)
else:
    st.info(t("no_data"))

# ---------------------------------------------------------
# Zeitreihe: Preis pro kg über die Jahre
# ---------------------------------------------------------
st.subheader(t("chart_ppk_per_year"))

ppk_year = (
    df.groupby("year")
    .apply(lambda x: x["price"].sum() / x["netweight"].sum() if x["netweight"].sum() > 0 else None)
    .reset_index(name="price_per_kg")
)

fig_ppk = px.line(
    ppk_year,
    x="year",
    y="price_per_kg",
    markers=True,
    labels={"year": "", "price_per_kg": "USD/kg"}
)

st.plotly_chart(fig_ppk, use_container_width=True)

# ---------------------------------------------------------
# Year-over-Year Veränderung
# ---------------------------------------------------------
st.subheader(t("chart_yoy"))

yoy_df = df.groupby("year", as_index=False)["price"].sum()
yoy_df["prev"] = yoy_df["price"].shift(1)
yoy_df["yoy_pct"] = (yoy_df["price"] - yoy_df["prev"]) / yoy_df["prev"] * 100

fig_yoy = px.bar(
    yoy_df,
    x="year",
    y="yoy_pct",
    labels={"year": "", "yoy_pct": "%"}
)

st.plotly_chart(fig_yoy, use_container_width=True)

# ---------------------------------------------------------
# 1_Analyse.py 
# Zweisprachige Version (Deutsch / Englisch)
# Enthält:
# - Risiko-Karte
# - CSV-Download
# - Detailtabelle
# - Sidebar-Logout
# ---------------------------------------------------------


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

# ---------------------------------------------------------
# Sidebar: Logout
# ---------------------------------------------------------
with st.sidebar:
    st.header(t("nav_header"))
    st.success(f"{t('logged_in_as')} {st.session_state['username']}")

    if st.button(t("logout")):
        st.session_state.clear()
        st.switch_page("pages/login.py")

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