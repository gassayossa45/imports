# ---------------------------------------------------------
# 2_Risikoanalyse.py — Zweisprachige Version (DE/EN)
# ---------------------------------------------------------

import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
from utils import t   # Übersetzungsfunktion
import pycountry



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


st.markdown("""
<style>
    /* Alle Präsentationsseiten aus der Sidebar entfernen */
    section[data-testid="stSidebarNav"] li a[href*="presentation_"] {
        display: none !important;
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
# Zugriffsschutz (zweisprachig)
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
# Titel (zweisprachig)
# ---------------------------------------------------------
st.title(t("risk_title"))

df = load_data()

#Sidebar trennen
st.sidebar.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Filter (zweisprachig)
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
    df["country_name"].isin(countries) &
    df["product_name"].isin(products)
]

# ---------------------------------------------------------
# Neue Summary-Kennzahlen + HHI + Risiko-Ampel
# ---------------------------------------------------------

st.subheader(t("summary_overview_title"))

if filtered.empty:
    st.info(t("summary_no_data"))
else:
    # -----------------------------
    # HHI-Berechnung
    # -----------------------------
    grouped = filtered.groupby(["product_name", "country_name"])["price"].sum().reset_index()
    grouped["share"] = grouped.groupby("product_name")["price"].transform(lambda x: x / x.sum())
    grouped["hhi_share"] = grouped["share"] ** 2

    # HHI pro Produkt
    hhi_product = grouped.groupby("product_name")["hhi_share"].sum().reset_index()

    # Gesamt-HHI (Durchschnitt)
    hhi_total = hhi_product["hhi_share"].mean()

    # Diversität
    diversity = 1 - hhi_total

    # Anzahl Länder
    num_countries = filtered["country_name"].nunique()

    # Anzahl Produkte
    num_products = filtered["product_name"].nunique()

    # -----------------------------
    # Kennzahlen (zweisprachig)
    # -----------------------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        label=t("summary_hhi_label"),
        value=f"{hhi_total:.3f}",
        help=t("summary_hhi_help")
    )

    col2.metric(
        label=t("summary_diversity_label"),
        value=f"{diversity:.3f}",
        help=t("summary_diversity_help")
    )

    col3.metric(
        label=t("summary_countries_label"),
        value=num_countries,
        help=t("summary_countries_help")
    )

    col4.metric(
        label=t("summary_products_label"),
        value=num_products,
        help=t("summary_products_help")
    )

    # -----------------------------
    # Risiko-Ampel
    # -----------------------------
    if hhi_total < 0.30:
        risk_level = t("risk_low")
        color = "#2ecc71"  # green
    elif hhi_total < 0.50:
        risk_level = t("risk_medium")
        color = "#f1c40f"  # yellow
    else:
        risk_level = t("risk_high")
        color = "#e74c3c"  # red

    st.markdown(
        f"""
        <div style='padding:15px; background-color:{color}; color:white; border-radius:8px; margin-top:20px;'>
            <h3 style='margin:0;'>{t("summary_risk_title")}: {risk_level}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------
    # Narrative Interpretation
    # -----------------------------
    st.markdown("### " + t("summary_interpretation_title"))

    summary_text = t("summary_interpretation").format(
        hhi=f"{hhi_total:.3f}",
        diversity=f"{diversity:.3f}",
        countries=num_countries,
        products=num_products
    )

    st.write(summary_text)



# Risiko – Choropleth Map
st.subheader (t("risk_map_title"))

if not filtered.empty:

    # Risiko aggregieren
    risk = filtered.groupby("country_name", as_index=False)["price"].sum()
    total_risk = risk["price"].sum()
    risk["dependency"] = risk["price"] / total_risk if total_risk > 0 else 0

    # ISO3 automatisch generieren
    def country_to_iso3(name):
        try:
            return pycountry.countries.lookup(name).alpha_3
        except:
            return None

    risk["iso3"] = risk["country_name"].apply(country_to_iso3)

    # Choropleth Map erzeugen
    fig_map = px.choropleth(
        risk,
        locations="iso3",
        color="dependency",
        hover_name="country_name",
        color_continuous_scale="Reds",
        projection="natural earth",
        #title=t("risk_map_title")
    )

    fig_map.update_layout(
        margin=dict(l=0, r=0, t=50, b=0),
        coloraxis_colorbar=dict(title=t("dependency"))
    )
    fig_map.update_layout(
    hoverlabel=dict(
        font_size=16,
        font_family="Arial",
        bgcolor="black",
        font_color="white",
        bordercolor="#1E3A5F"
    )
    )
    st.plotly_chart(fig_map, use_container_width=True)

else:
    st.info(t("no_data"))


# HHI
st.subheader(t("hhi_title"))
if not filtered.empty:
    shares = filtered.groupby("country_name")["price"].sum() / filtered["price"].sum()
    hhi_value = (shares ** 2).sum()
    st.metric("HHI-Index", f"{hhi_value:.3f}")
else:
    st.info("Keine Daten für HHI-Berechnung.")

# HHI je Produkt und Land berechnen
grouped = filtered.groupby(["product_name", "country_name"])["price"].sum().reset_index()

# Marktanteil je Land für jedes Produkt
grouped["share"] = grouped.groupby("product_name")["price"].transform(lambda x: x / x.sum())

# HHI-Anteil je Land
grouped["hhi_share"] = grouped["share"] ** 2

# Finale Tabelle
hhi_detail = grouped[["product_name", "country_name", "hhi_share"]]

st.subheader(t("hhi_country_product"))

# Fall 1: Keine Auswahl
if not selected_products:
    st.info(t("select_at_least_one_product"))
    st.stop()

# Fall 2: Ein Produkt → Bar Chart
if len(selected_products) == 1:
    produkt = selected_products[0]
    df_prod = hhi_detail[hhi_detail["product_name"] == produkt]

    if df_prod.empty:
        st.warning(t("no_data_for_product"))
    else:
        fig = px.bar(
            df_prod,
            x="country_name",
            y="hhi_share",
            color="country_name",
            title=f"HHI-Anteil je Land für {produkt}",
            labels={"country_name": "Land", "hhi_share": "HHI-Anteil"}
        )
        fig.update_layout(showlegend=False)
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

# Fall 3: Mehrere Produkte → Heatmap
else:
    df_multi = hhi_detail[hhi_detail["product_name"].isin(selected_products)]
    pivot = df_multi.pivot(index="product_name", columns="country_name", values="hhi_share")

    fig = px.imshow(
        pivot,
        color_continuous_scale="Reds",
        aspect="auto",
        labels={"color": "HHI-Anteil"},
        title="HHI-Heatmap je Produkt und Land"
    )
    fig.update_layout(
    hoverlabel=dict(
        font_size=16,
        font_family="Arial",
        bgcolor="black",
        font_color="white",
        bordercolor="#1E3A5F"
    )
)


    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# HHI-Trend
# ---------------------------------------------------------
st.subheader(t("hhi_trend_title"))

trend = (
    filtered.groupby(["year", "country_name"])["price"].sum()
    .groupby(level=0)
    .apply(lambda x: ((x / x.sum()) ** 2).sum())
    .reset_index(name="hhi")
)

fig_trend = px.line(trend, x="year", y="hhi", markers=True)

# Tooltip lesbarer machen
fig_trend.update_layout(
    hoverlabel=dict(
        font_size=16,
        font_family="Arial",
        bgcolor="black",
        font_color="white",
        bordercolor="#1E3A5F"
    )
)


st.plotly_chart(fig_trend, use_container_width=True)

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