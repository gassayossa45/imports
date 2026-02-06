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

st.markdown("""
<style>

    /* Hauptcontainer – wieder zentriert */
    .block-container {
        padding-top: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 1100px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    /* Titelbalken */
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

    /* Inhalt */
    .slide-content {
        padding: 60px 120px;
        font-size: 22px;
        line-height: 1.6;
        padding-bottom: 120px !important; /* WICHTIG: Abstand für Footer */
    }

    /* Titel der Folien */
    .slide-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 20px;
        color: #003366;
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
        background: linear-gradient(90deg, #00264d, #004080);
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

st.markdown("""
<style>

    /* Hauptcontainer – wieder zentriert */
    .block-container {
        padding-top: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 1100px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    /* Titelbalken */
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

    /* Inhalt */
    .slide-content {
        padding: 60px 120px;
        font-size: 22px;
        line-height: 1.6;
        padding-bottom: 120px !important; /* WICHTIG: Abstand für Footer */
    }

    /* Titel der Folien */
    .slide-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 20px;
        color: #003366;
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
        background: linear-gradient(90deg, #00264d, #004080);
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
st.markdown(f"<div class='top-bar'>{t('pres_analysis_title')}</div>", unsafe_allow_html=True)

# Inhalt
st.markdown("<div class='slide-content fade-in'>", unsafe_allow_html=True)

slides = [
    ("1 – " + t("section_intro"), t("pres_1_intro")),
    ("2 – " + t("section_motivation"), t("pres_2_motivation")),
    ("3 – " + t("section_goal"), t("pres_3_goal")),
    ("4 – " + t("section_data"), t("pres_4_data")),
    ("5 – " + t("section_overview"), t("pres_5_overview")),
    ("6 – " + t("section_kpis"), t("pres_6_kpis")),
]

for title, text in slides:
    st.markdown(f"<div class='slide-title'>{title}</div>", unsafe_allow_html=True)
    st.write(text)

st.markdown("</div>", unsafe_allow_html=True)


# Button
#if st.button(t("pres_next_risk")):
    #st.switch_page("pages/2_Risikoanalyse.py")

# Button
if st.button(t("pres_end")):
    st.switch_page("Startseite.py")

# Sticky Footer
st.markdown(
    f"<div class='footer-bar'>{t('footer_project_info')}</div>",
    unsafe_allow_html=True
)