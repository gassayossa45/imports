import streamlit as st
from utils import register_user
import time

# register.py
#st.set_page_config(page_title="Registrierung", layout="centered")

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

st.title("📝 Registrierung")

username = st.text_input("Benutzername")
email = st.text_input("E-Mail")
password = st.text_input("Passwort", type="password")

if st.button("Registrieren"):
    try:
        register_user(username, email, password)
        st.success("Registrierung erfolgreich! Du kannst dich jetzt einloggen.")
        st.balloons()
        time.sleep(1.2)
        st.switch_page("pages/login.py")
    except Exception as e:
        st.error("Fehler: Benutzername oder E-Mail existiert bereits.")