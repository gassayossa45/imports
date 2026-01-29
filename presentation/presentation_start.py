# presentation_start.py

import streamlit as st
from utils import t

st.markdown("""
<style>

    /* Vollbild-Layout wie PowerPoint */
    .block-container {
        padding-top: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }

    /* Farbiger Balken oben */
    .top-bar {
        width: 100%;
        height: 80px;
        background: linear-gradient(90deg, #003366, #0055A4);
        color: white;
        display: flex;
        align-items: center;
        padding-left: 40px;
        font-size: 32px;
        font-weight: 600;
        letter-spacing: 1px;
    }

    /* Seitencontainer wie PowerPoint */
    .slide-content {
        padding: 60px 120px;
        font-size: 22px;
        line-height: 1.6;
    }

    /* Überschriften */
    .slide-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 20px;
        color: #003366;
    }

    .slide-subtitle {
        font-size: 28px;
        font-weight: 500;
        margin-bottom: 40px;
        color: #0055A4;
    }

    /* Fade-in Animation */
    .fade-in {
        animation: fadeIn 0.8s ease-in-out;
    }

    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

</style>
""", unsafe_allow_html=True)


# Sprache sicherstellen
if "lang" not in st.session_state:
    st.session_state["lang"] = "de"

# Präsentationsseiten aus Sidebar entfernen
st.markdown("""
<style>
    section[data-testid="stSidebarNav"] li a[href*="presentation_"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar komplett ausblenden
st.markdown("""
<style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="stToolbar"] {display: none;}
    .block-container {padding-top: 2rem;}
</style>
""", unsafe_allow_html=True)

st.session_state["presentation_mode"] = True

st.set_page_config(page_title="Presentation", layout="wide")

# Inhalt
st.markdown(f"""
<div style='text-align:center; padding-top:80px;'>
    <h1 style='font-size:60px;'>{t("presentation_start_title")}</h1>
    <h3 style='color:#888;'>{t("presentation_start_subtitle")}</h3>
    <p style='font-size:20px; margin-top:30px;'>
        {t("presentation_start_description")}
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button(t("presentation_start_button"), use_container_width=True):
        st.switch_page("pages/1_Analyse.py")