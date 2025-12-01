import streamlit as st
import time
import random
import json
import re

# ---------------------- PAGE SETUP ----------------------
st.set_page_config(
    page_title="Transtornos Mentais Relacionados ao Trabalho no município de Campinas - SP",
    page_icon="📜",
    layout="wide"
)

# ---------------------- STYLES ----------------------
st.markdown("""
<style>
.stApp {
    background-color: #121212;
    color: #f5f5f5;
}

.red {
    color: #ff5555;
    font-weight: bold;
}

/* Fade animations */
@keyframes fadeIn {
    0%   { opacity: 0; }
    100% { opacity: 1; }
}

@keyframes fadeOut {
    0%   { opacity: 1; }
    100% { opacity: 0; }
}

/* Classes */
.fade-in {
    animation: fadeIn 2s forwards;
}

.fade-out {
    animation: fadeOut 2s forwards;
}

/* Main text style */
.main-text {
    font-size: 2rem;
    text-align: center;
    color: #e0e0e0;
    padding: 40px;
    /* keep height so layout doesn't jump when text changes */
    min-height: 3.5rem;
}
</style>
""", unsafe_allow_html=True)

def get_text(n_iteration):
    with open("inputs/sentences_high.json", "r") as file:
        sentences_high = json.load(file)

    with open("inputs/sentences_avg.json", "r") as file:
        sentences_avg = json.load(file)

    if n_iteration < len(sentences_high):
        text = sentences_high[n_iteration]
    else:
        text = random.choice(sentences_avg)  # your prebuilt list of sentences

    # Replace <VAR>...</VAR> with red span
    text = re.sub(r"<VAR>(.*?)</VAR>", r"<span class='red'>\1</span>", text)
    text = text.replace('\n', '<br>')
    return text


# ---------------------- HEADER ----------------------
st.markdown("<h1>Transtornos Mentais Relacionados ao Trabalho no Município de Campinas</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <p style='
        text-align: left;
        color: #b0b0b0;
        font-size: 1rem;
        margin-left: 12px;
        margin-top: -10px;
    '>
        Histórias reais de pessoas que sofreram deste agravo, com base em dados do SINAN*
    </p>
    """,
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
        * Mesmo que o banco não contenha informações pessoalmente identificáveis, as entradas foram embaralhadas aleatoriamente para preservar a privacidade dos casos.<BR>
        ** Nomes gerados aleatoriamente para fins ilustrativos.
    </p>
    """,
    unsafe_allow_html=True
)


# Placeholder for the changing text
placeholder = st.empty()

n_iteration = 0

# Initialize state
if "current_text" not in st.session_state:
    st.session_state.current_text = get_text(n_iteration)



def render(text, css_class):
    """Render the given text with the provided CSS class into the same placeholder."""
    html = f"<div class='main-text {css_class}'>{text}</div>"
    placeholder.markdown(html, unsafe_allow_html=True)
    placeholder.markdown(html, unsafe_allow_html=True)


# Initially show the current text (fade-in on first render)
render(st.session_state.current_text, "fade-in")

# ---------------------- REFRESH LOOP (10s cycle) ----------------------
while True:
    # pick a new text different from current
    new_text = st.session_state.current_text
    attempt = 0
    while new_text == st.session_state.current_text and attempt < 10:
        new_text = get_text(n_iteration)
        attempt += 1

    # FADE OUT current text (apply fade-out to the same existing text)
    render(st.session_state.current_text, "fade-out")
    time.sleep(2)   # wait for fade-out to finish

    # Replace with new text and FADE IN
    st.session_state.current_text = new_text
    render(st.session_state.current_text, "fade-in")
    time.sleep(12)   # visible time (2s fade-in + 6s visible + next 2s fade-out = 10s)
    n_iteration += 1
