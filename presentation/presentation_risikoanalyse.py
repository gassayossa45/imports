import streamlit as st
from utils import t

if "lang" not in st.session_state:
    st.session_state["lang"] = "de"

# PowerPoint Layout
st.markdown("""
<style>
    .block-container {
        padding-top: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
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
    }
    .slide-content {
        padding: 60px 120px;
        font-size: 22px;
        line-height: 1.6;
    }
    .slide-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 20px;
        color: #660000;
    }
    .fade-in {
        animation: fadeIn 0.8s ease-in-out;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
</style>
""", unsafe_allow_html=True)

st.markdown(f"<div class='top-bar'>{t('pres_risk_title')}</div>", unsafe_allow_html=True)
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

if st.button(t("pres_next_summary")):
    st.switch_page("pages/presentation_summary.py")