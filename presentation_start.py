import streamlit as st
from utils import t



st.markdown("""
<style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="stToolbar"] {display: none;}
    .block-container {padding-top: 2rem;}
</style>
""", unsafe_allow_html=True)

st.session_state["presentation_mode"] = True

st.set_page_config(page_title="Presentation", layout="wide")

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
        st.switch_page("pages/1_analyse.py")