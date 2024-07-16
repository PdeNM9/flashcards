import streamlit as st

from auth import load_data


# Página de login
def login():
    st.title('Flashcards ENAM - Login')

    if 'login_attempted' not in st.session_state:
        st.session_state.login_attempted = False

    if not st.session_state.login_attempted:
        username = st.text_input('Usuário', key='login_username')
        password = st.text_input('Senha', type='password', key='login_password')

        if st.button('Entrar', key='login_button'):
            st.session_state.login_attempted = True
            if username == '' and password == '':
                st.session_state.logged_in = True
                st.session_state.data = load_data()
                st.rerun()
            else:
                st.session_state.login_attempted = False
                st.error('Usuário ou senha incorretos.')
    else:
        st.write("Bem-vindo ao Flashcards ENAM!")
