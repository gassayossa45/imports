import streamlit as st
from PIL import Image

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(
    page_title="Critical Raw Materials – Dashboard",
    layout="wide"
)

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
# ---------------------------------------------------------
# Sidebar Navigation (Login / Registrierung / Logout)
# ---------------------------------------------------------
with st.sidebar:
    st.header("Navigation")

    # Wenn NICHT eingeloggt → Login + Registrierung anzeigen
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        if st.button("🔐 Login"):
            st.switch_page("pages/login.py")

        if st.button("📝 Registrierung"):
            st.switch_page("pages/register.py")

    # Wenn eingeloggt → Username + Logout anzeigen
    else:
        st.success(f"Angemeldet als {st.session_state['username']}")
        if st.button("🚪 Logout"):
            st.session_state.clear()
            st.switch_page("pages/login.py")

# ---------------------------------------------------------
# Zugriffsschutz: Nur sichtbar, wenn eingeloggt
# ---------------------------------------------------------
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("Bitte zuerst einloggen.")
    st.stop()

# ---------------------------------------------------------
# Logo laden und anzeigen
# ---------------------------------------------------------
logo = Image.open("images/import_logo_modi.jpg")
logo = logo.resize((1050, 200))  # Höhe reduziert
st.image(logo)

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
# Welcome Content
# ---------------------------------------------------------
st.title("🌍 Critical Raw Materials – Import & Risiko Dashboard")

st.markdown("""
Willkommen zu meinem Dashboard-Projekt über **kritische Rohstoffe**.

Dieses Multi-Page-Dashboard besteht aus:

1. **Analyse** – Deskriptive Analyse der Importe (Werte, Mengen, Preis pro kg, Zeitreihen, Heatmap).
2. **Risikoanalyse** – Konzentrationsrisiken, Abhängigkeiten, China-Exposure, HHI-Trends.
3. **Summary** – Top-5 Länder je Produkt, Top-5 Produkte je Jahr, automatische Insights.

Die Daten basieren auf einem **Star-Schema** in PostgreSQL mit:
- `dim_years`, `dim_countries`, `dim_products`
- `fact_imports` (Mengen, Gewichte, Werte)

Nutzen Sie die Seitenleiste links, um zwischen den Dashboards zu wechseln.
""")

if not filtered.empty:

    # Risiko aggregieren
    risk = filtered.groupby("country_name", as_index=False)["price"].sum()
    total_risk = risk["price"].sum()
    risk["dependency"] = risk["price"] / total_risk if total_risk > 0 else 0
    risk["iso3"] = risk["country_name"].apply(country_to_iso3)
    # ISO3-Codes hinzufügen (risk muss iso3 enthalten)
    # Beispiel: risk = risk.merge(country_codes_df, on="country_name", how="left")

    # Risiko – Choropleth Map
