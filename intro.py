import streamlit as st

# ---- PAGE SETUP ----
st.set_page_config(page_title="Transtornos Mentais Relacionados ao Trabalho no município de Campinas - SP", layout="wide")

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

    /* Headings */
    [data-testid="stMarkdownContainer"] h1 {
        text-align: left !important;
        font-family: 'Trebuchet MS', sans-serif;
        color: #f0f0f0 !important;
        font-size: 1.6rem !important;
        margin-top: -3rem !important;
        margin-left: -0.5rem !important;
        margin-bottom: 0.3rem !important;
    }

    p.custom-text {
        color: #b0b0b0 !important;
        font-size: 2.0rem;
        line-height: 1.6 !important;
        margin-left: 12px;
        margin-top: 30px;
        text-align: left;
    }
""", unsafe_allow_html=True)

# ---- PAGE CONTENT ----
st.markdown("<h1>Transtornos Mentais Relacionados ao Trabalho no Município de Campinas</h1>", unsafe_allow_html=True)

st.markdown(
    "<p class='custom-text'>A notificação de Transtornos Mentais Relacionados ao Trabalho só se tornou obrigatória em Agosto de 2014.</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='custom-text'>De acordo com dados do SINAN*, de Setembro de 2024 a Março de 2025 foram <span style='color:#ff5555;'>84 casos reportados</span>, apenas no município de Campinas.</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='custom-text'>O objetivo deste trabalho é contar algumas dessas <span style='color:#ff5555;'>histórias</span>.</p>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='
        position: fixed;
        bottom: 10px;
        width: 100%;
        text-align: left;
        font-size: 1.2rem;
        color: #888888;
    '>
        * Sistema de Informação de Agravos de Notificação
    </p>
    """,
    unsafe_allow_html=True
)

def clear_iterations():
    with open('iteration.txt', 'w') as f:
        f.write('0')

clear_iterations()
