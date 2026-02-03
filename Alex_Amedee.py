# ---------------------------------------------------------
# Startseite.py — Zweisprachige Version (DE/EN)
# ---------------------------------------------------------

import streamlit as st
from PIL import Image
from utils import t   # Übersetzungsfunktion
import os
from supabase import create_client

#url = os.getenv("SUPABASE_URL")
#key = os.getenv("SUPABASE_ANON_KEY")

#supabase = create_client(url, key)


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

st.markdown("""
<style>
/* Größere Schrift für alle Markdown-Absätze */
.main p {
    font-size: 22px !important;
    line-height: 1.6 !important;
}
</style>
""", unsafe_allow_html=True)
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
logo = logo.resize((850, 200))
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
