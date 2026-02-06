import streamlit as st
from utils import t

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(
    page_title= t("home_title"),
    layout="wide"
)

if "lang" not in st.session_state:
    st.session_state["lang"] = "de"

# ---------------------------------------------------------
# Zugriffsschutz
# ---------------------------------------------------------
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning(t("login_required"))
    st.switch_page("pages/login.py")
    st.stop()

# Sidebar komplett ausblenden
st.markdown("""
<style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="stSidebarNav"] {display: none;}
    [data-testid="stToolbar"] {display: none;}
</style>
""", unsafe_allow_html=True)

# PowerPoint Layout + Sticky Footer
st.markdown("""
<style>

    /* Hauptcontainer */
    .block-container {
        padding-top: 1rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 1100px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    /* Titelbalken */
    .top-bar {
        width: 100%;
        height: 80px;
        background: linear-gradient(90deg, #660000, #990000);
        color: white;
        display: flex;
        align-items: center;
        padding-left: 40px;
        font-size: 32px;
        font-weight: 600;
        letter-spacing: 1px;
        box-sizing: border-box;
    }

    /* Inhalt */
    .slide-content {
        padding: 40px 20px;
        font-size: 22px;
        line-height: 1.6;
        padding-bottom: 120px !important; /* Abstand für Sticky Footer */
    }

    /* Titel der Folien */
    .slide-title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 20px;
        color: #660000;
    }

    /* Fade-In Animation */
    .fade-in {
        animation: fadeIn 0.8s ease-in-out;
    }

    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    /* Sticky Footer */
    .footer-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 55px;
        background: linear-gradient(90deg, #660000, #990000); /* Risiko-Farbe */
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

    /* Footer Animation */
    @keyframes footerFadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

</style>
""", unsafe_allow_html=True)

# Titel
st.markdown(f"<div class='top-bar'>{t('pres_risk_title')}</div>", unsafe_allow_html=True)

# Inhalt
st.markdown("<div class='slide-content fade-in'>", unsafe_allow_html=True)

slides = [
    ("7 – " + t("section_countries"), t("pres_7_countries")),
    ("8 – " + t("section_heatmap"), t("pres_8_heatmap")),
    ("9 – " + t("section_hhi"), t("pres_9_hhi")),
    ("10 – " + t("section_summary"), t("pres_10_summary")),
    ("11 – " + t("section_batteries"), t("pres_11_batteries")),
    ("12 – " + t("section_industry"), t("pres_12_industry")),
]

for title, text in slides:
    st.markdown(f"<div class='slide-title'>{title}</div>", unsafe_allow_html=True)
    st.write(text)

st.markdown("</div>", unsafe_allow_html=True)


# Button
#if st.button(t("pres_next_summary")):
    #st.switch_page("pages/3_Summary.py")

# Button
if st.button(t("pres_end")):
    st.switch_page("Startseite.py")


# Sticky Footer
st.markdown(
    f"<div class='footer-bar'>{t('footer_project_info')}</div>",
    unsafe_allow_html=True
)