import streamlit as st

st.set_page_config(page_title="Flashcards ENAM!", page_icon="📚")

from login import login
from pages import flashcards_page, selection_page

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    if 'assunto' not in st.session_state:
        selection_page()
    else:
        flashcards_page()
else:
    login()
