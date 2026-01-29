# ---------------------------------------------------------
# Startseite.py — Zweisprachige Version (DE/EN)
# ---------------------------------------------------------

import streamlit as st
from PIL import Image
from utils import t   # Übersetzungsfunktion

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(
    page_title="Critical Raw Materials – Dashboard",
    layout="wide"
)

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
# Zugriffsschutz
# ---------------------------------------------------------
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning(t("login_or_register_required"))
    st.stop()

# ---------------------------------------------------------
# Logo
# ---------------------------------------------------------
logo = Image.open("images/import_logo_modi.jpg")
logo = logo.resize((1050, 200))
st.image(logo)

# ---------------------------------------------------------
# Titel
# ---------------------------------------------------------
st.title(t("home_title"))

# ---------------------------------------------------------
# Willkommenstext (zweisprachig)
# ---------------------------------------------------------
st.markdown(t("home_intro"))
st.markdown(t("home_description"))

st.markdown(t("home_point_analysis"))
st.markdown(t("home_point_risk"))
st.markdown(t("home_point_summary"))

st.markdown(t("home_data_basis"))
st.markdown(t("home_data_tables"))

st.markdown(t("home_sidebar_hint"))