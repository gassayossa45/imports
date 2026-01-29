# register.py
# ---------------------------------------------------------
# Zweisprachige Registrierungsseite (Deutsch / Englisch)
# Alle Texte werden über die t()-Funktion aus utils.py geladen.
# ---------------------------------------------------------

import streamlit as st
from utils import register_user, t
import time

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
st.title(t("register_title"))

# ---------------------------------------------------------
# Eingabefelder (zweisprachig)
# ---------------------------------------------------------
username = st.text_input(t("username"))
email = st.text_input(t("email"))
password = st.text_input(t("password"), type="password")

# ---------------------------------------------------------
# Registrierungs-Button
# ---------------------------------------------------------
if st.button(t("register_button")):
    try:
        register_user(username, email, password)

        st.success(t("register_success"))
        st.balloons()
        time.sleep(1.2)

        # Weiterleitung zur Login-Seite
        st.switch_page("pages/login.py")

    except Exception as e:
        # Fehlertext zweisprachig
        st.error(t("register_error"))