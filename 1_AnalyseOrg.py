import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
import pycountry

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

# Styling
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

# DB-Verbindung
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

st.title("📊 Analyse deutscher– Importe kritischer Rohstoffe")

df = load_data()

# Sidebar Filter
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

# KPIs
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
        <h4 style="color:white;">Gesamtwert (USD)</h4>
        <h2 style="color:white;">{formatted_value}</h2>
    </div>
    """,
    unsafe_allow_html=True
)

col2.markdown(
    f"""
    <div style="background-color:#1E3A5F; padding:16px; border-radius:10px; text-align:center;">
        <h4 style="color:white;">Gesamtgewicht (kg)</h4>
        <h2 style="color:white;">{formatted_weight}</h2>
    </div>
    """,
    unsafe_allow_html=True
)

col3.markdown(
    f"""
    <div style="background-color:#1E3A5F; padding:16px; border-radius:10px; text-align:center;">
        <h4 style="color:white;">Ø Preis (USD)</h4>
        <h2 style="color:white;">{formatted_avg}</h2>
    </div>
    """,
    unsafe_allow_html=True
)

col4.markdown(
    f"""
    <div style="background-color:{kpi_color}; padding:16px; border-radius:10px; text-align:center;">
        <h4 style="color:white;">Preis pro kg (USD/kg)</h4>
        <h2 style="color:white;">{formatted_ppk}</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# Charts Länder & Produkte
colA, colB = st.columns(2)

with colA:
    st.subheader("Importwert nach Ländern")
    if not filtered.empty:
        by_country = filtered.groupby("country_name", as_index=False)["price"].sum()
        fig_country = px.bar(by_country, x="country_name", y="price")
        st.plotly_chart(fig_country, use_container_width=True)
    else:
        st.info("Keine Daten für die aktuelle Filterauswahl.")

with colB:
    st.subheader("Importwert nach Produkten")
    if not filtered.empty:
        by_product = filtered.groupby("product_name", as_index=False)["price"].sum()
        fig_product = px.bar(by_product, x="product_name", y="price")
        fig_product.update_xaxes(tickangle=45)
        st.plotly_chart(fig_product, use_container_width=True)
    else:
        st.info("Keine Daten für die aktuelle Filterauswahl.")

# Zeitreihe Wert
st.subheader("Zeitreihe: Importwert pro Jahr")
if not filtered.empty:
    by_year = filtered.groupby("year", as_index=False)["price"].sum()
    fig_year = px.line(by_year, x="year", y="price", markers=True)
    st.plotly_chart(fig_year, use_container_width=True)
else:
    st.info("Keine Daten für die aktuelle Filterauswahl.")

# Zeitreihe Preis/kg
st.subheader("Zeitreihe: Preis pro kg über die Jahre")
ppk_year = (
    df.groupby("year")
    .apply(lambda x: x["price"].sum() / x["netweight"].sum() if x["netweight"].sum() > 0 else None)
    .reset_index(name="price_per_kg")
)
fig_ppk = px.line(ppk_year, x="year", y="price_per_kg", markers=True)
st.plotly_chart(fig_ppk, use_container_width=True)

# YoY
st.subheader("📉 Year-over-Year Veränderung (Importwert)")
yoy_df = df.groupby("year", as_index=False)["price"].sum()
yoy_df["prev"] = yoy_df["price"].shift(1)
yoy_df["yoy_pct"] = (yoy_df["price"] - yoy_df["prev"]) / yoy_df["prev"] * 100
fig_yoy = px.bar(yoy_df, x="year", y="yoy_pct")
st.plotly_chart(fig_yoy, use_container_width=True)



def country_to_iso3(name):
    try:
        return pycountry.countries.lookup(name).alpha_3
    except:
        return None

# Risiko – Choropleth Map
st.subheader("🌍 Geografische Risiko-Karte: Importabhängigkeit")

if not filtered.empty:

    # Risiko aggregieren
    risk = filtered.groupby("country_name", as_index=False)["price"].sum()
    total_risk = risk["price"].sum()
    risk["dependency"] = risk["price"] / total_risk if total_risk > 0 else 0

    # ISO3 automatisch generieren
    import pycountry
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
        title="Geografische Risiko-Karte: Importabhängigkeit"
    )

    fig_map.update_layout(
        margin=dict(l=0, r=0, t=50, b=0),
        coloraxis_colorbar=dict(title="Abhängigkeit")
    )

    st.plotly_chart(fig_map, use_container_width=True)

else:
    st.info("Keine Daten für die aktuelle Filterauswahl.")
# CSV
st.subheader("📥 Daten herunterladen")
csv = filtered.to_csv(index=False).encode("utf-8")
st.download_button(
    label="CSV herunterladen",
    data=csv,
    file_name="import_data_filtered.csv",
    mime="text/csv"
)

st.subheader("Detailtabelle")
st.dataframe(filtered.sort_values(["year", "country_name", "product_name"]))

 # Wenn eingeloggt → Username + Logout anzeigen
 
with st.sidebar:
    st.header("Navigation")
    st.success(f"Angemeldet als {st.session_state['username']}")
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.switch_page("pages/login.py")