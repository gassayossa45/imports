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
        background: linear-gradient(90deg, #004d26, #00994d);
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
        color: #004d26;
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

st.markdown(f"<div class='top-bar'>{t('pres_summary_title')}</div>", unsafe_allow_html=True)
st.markdown("<div class='slide-content fade-in'>", unsafe_allow_html=True)

slides = [
    ("13 – " + t("section_policy"), t("pres_13_policy")),
    ("14 – " + t("section_recommendations"), t("pres_14_recommendations")),
    ("15 – " + t("section_conclusion"), t("pres_15_conclusion")),
]

for title, text in slides:
    st.markdown(f"<div class='slide-title'>{title}</div>", unsafe_allow_html=True)
    st.write(text)

st.markdown("</div>", unsafe_allow_html=True)

if st.button(t("pres_end")):
    st.switch_page("pages/1_Analyse.py")