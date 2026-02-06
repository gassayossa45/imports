# login.py
# ---------------------------------------------------------
# Zweisprachige Login-Seite (Deutsch / Englisch)
# Alle Texte werden über die t()-Funktion aus utils.py geladen.
# ---------------------------------------------------------

import streamlit as st
from utils import check_user, t
import time

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(
    page_title= t("home_title"),
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
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Titel (zweisprachig)
# ---------------------------------------------------------
st.title(t("login_title"))

# ---------------------------------------------------------
# Eingabefelder (zweisprachig)
# ---------------------------------------------------------
username = st.text_input(t("username"))
password = st.text_input(t("password"), type="password")

# ---------------------------------------------------------
# Login-Button
# ---------------------------------------------------------
if st.button(t("login_button")):

    if check_user(username, password):
        # Login erfolgreich
        st.session_state["logged_in"] = True
        st.session_state["username"] = username

        st.success(t("login_success"))
        st.balloons()
        time.sleep(1.2)

        # Weiterleitung zur Startseite
        st.switch_page("Startseite.py")

    else:
        # Fehlermeldung (zweisprachig)
        st.error(t("login_error"))