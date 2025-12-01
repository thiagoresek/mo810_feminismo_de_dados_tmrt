import streamlit as st

# ---- CUSTOM STYLES ----
st.markdown("""
    <style>
    /* Main background */
    .stApp {    
        background-color: #121212;
        color: #f5f5f5;
    }

    /* Header bar */
    header[data-testid="stHeader"] {
        background-color: #121212;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #1e1e1e;
        color: #f5f5f5;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
""", unsafe_allow_html=True)

intro_page = st.Page("intro.py", title="Introdução")
stories_page = st.Page("data_visualization.py", title="Histórias")

pg = st.navigation([intro_page, stories_page])
# st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()