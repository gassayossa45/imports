import streamlit as st
from utils import check_user
import time

#login.py

#st.set_page_config(page_title="Login", layout="centered")

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

st.title("🔐 Login")

username = st.text_input("Benutzername")
password = st.text_input("Passwort", type="password")

if st.button("Login"):
    if check_user(username, password):
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.success("Login erfolgreich!")
        st.balloons()
        time.sleep(1.2)
        st.switch_page("Startseite.py")
        with st.sidebar:
            st.header("Navigation")
            st.success(f"Angemeldet als {st.session_state['username']}")
            if st.button("🚪 Logout"):
                st.session_state.clear()
                st.switch_page("pages/login.py")

    else:
        st.error("Benutzername oder Passwort falsch.")