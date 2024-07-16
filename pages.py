import streamlit as st


# Página de seleção de assunto
def selection_page():
    st.title('Flashcards ENAM - Assuntos:')
    data = st.session_state.data
    assuntos = ['TODOS'] + data['Assunto'].unique().tolist()
    assunto = st.selectbox('Selecione o Assunto', assuntos)

    if st.button('Iniciar'):
        st.session_state.assunto = assunto
        st.rerun()

# Página de exibição de flashcards
def flashcards_page():
    st.title('Flashcards ENAM - Flashcards')
    st.write('\n')
    data = st.session_state.data
    assunto = st.session_state.assunto

    # Filtrar flashcards que têm conteúdo não vazio nas colunas "Frente" e "Verso"
    data = data.dropna(subset=['Frente', 'Verso'])
    data = data[(data['Frente'] != '') & (data['Verso'] != '')]

    if assunto != 'TODOS':
        data = data[data['Assunto'] == assunto]

    if len(data) == 0:
        st.write("Nenhum flashcard disponível.")
        return

    if 'index' not in st.session_state:
        st.session_state.index = 0
    if 'show_front' not in st.session_state:
        st.session_state.show_front = True
    if 'button_style' not in st.session_state:
        st.session_state.button_style = 'primary'

    flashcard = data.iloc[st.session_state.index]

    st.write('\n')
    st.write('\n')
    st.write('\n')

    col1, col2 = st.columns([1, 1])

    with col2:
        if st.button('Próximo', type='secondary'):
            st.session_state.index += 1
            if st.session_state.index >= len(data):
                st.session_state.index = 0
            st.session_state.show_front = True
            st.rerun()

    with col1:
        button_label = 'Virar' if st.session_state.show_front else 'Mostrar Frente'

        if st.button(button_label, key='flip_button', type='primary'):
            st.session_state.show_front = not st.session_state.show_front
            st.rerun()


    st.write(f'**Assunto:** {flashcard["Assunto"]}')
    st.write('\n')

    card_content = flashcard["Frente"] if st.session_state.show_front else flashcard["Verso"]

    st.markdown(
        f"""
        <div style="border: 2px solid #4CAF50; padding: 20px; border-radius: 10px; text-align: center;">
            <p style="font-size: 28px;">{card_content}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.write('\n')
    st.write('\n')
    
    col3, col4 = st.columns([1, 1])
    
    with col3:
        if st.button('Voltar: INÍCIO !'):
            del st.session_state.assunto
            del st.session_state.index
            del st.session_state.show_front
            st.rerun()
            
    with col4:
        if st.button('Anterior', type='secondary'):
            st.session_state.index -= 1
            if st.session_state.index >= len(data):
                st.session_state.index = 0
            st.session_state.show_front = True
            st.rerun()
            