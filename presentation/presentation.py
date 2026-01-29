import streamlit as st
from utils import t

# Reihenfolge der Slides
SLIDES = ["start", "analysis", "risk", "summary"]

def render():
    params = st.experimental_get_query_params()
    slide = params.get("slide", ["start"])[0]

    # Sidebar & Toolbar ausblenden
    st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        [data-testid="stToolbar"] {display: none;}
        .block-container {padding-top: 2rem;}
    </style>
    """, unsafe_allow_html=True)

    # Fortschrittsbalken
    idx = SLIDES.index(slide)
    st.progress(idx / (len(SLIDES) - 1))
    st.caption(f"Slide {idx+1} / {len(SLIDES)}")

    # Tastatur-Navigation
    st.markdown(f"""
    <script>
    document.addEventListener('keydown', function(e) {{
        if (e.key === "ArrowRight") {{
            window.location.search = "?mode=presentation&slide={next_slide(slide)}";
        }}
        if (e.key === "ArrowLeft") {{
            window.location.search = "?mode=presentation&slide={prev_slide(slide)}";
        }}
    }});
    </script>
    """, unsafe_allow_html=True)

    # Inhalt rendern
    if slide == "start":
        render_start()
    elif slide == "analysis":
        render_analysis()
    elif slide == "risk":
        render_risk()
    elif slide == "summary":
        render_summary()


def next_slide(slide):
    idx = SLIDES.index(slide)
    return SLIDES[min(idx+1, len(SLIDES)-1)]

def prev_slide(slide):
    idx = SLIDES.index(slide)
    return SLIDES[max(idx-1, 0)]


# --- SLIDES ---

def render_start():
    st.title("🎬 Präsentation starten")
    st.write("Willkommen zur Präsentation.")
    if st.button("Weiter"):
        st.experimental_set_query_params(mode="presentation", slide="analysis")


def render_analysis():
    st.title(t("pres_analysis_title"))
    st.write(t("pres_1_intro"))
    st.write(t("pres_2_motivation"))
    if st.button("Weiter"):
        st.experimental_set_query_params(mode="presentation", slide="risk")


def render_risk():
    st.title(t("pres_risk_title"))
    st.write(t("pres_7_countries"))
    st.write(t("pres_8_heatmap"))
    if st.button("Weiter"):
        st.experimental_set_query_params(mode="presentation", slide="summary")


def render_summary():
    st.title(t("pres_summary_title"))
    st.write(t("pres_10_summary"))
    st.write(t("pres_15_conclusion"))
    if st.button("Beenden"):
        st.experimental_set_query_params(mode="dashboard")