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

    
    # Estilo CSS personalizado
    st.markdown("""
    <style>
        .stButton > button {
            width: 100%;
        }
        .full-width {
            width: 100%;
        }
        .card-content {
            border: 2px solid #4CAF50;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 28px;
            margin: 20px 0;
        }
        .centered {
            display: flex;
            justify-content: center;
        }
        .button-spacing {
            margin-top: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Botões superiores
    col_anterior, col_espaco, col_proximo = st.columns([1, 3, 1])

    with col_anterior:
        st.button('Anterior', key='anterior_btn', type='secondary')

    with col_proximo:
        st.button('Próximo', key='proximo_btn', type='secondary')

    # Conteúdo principal
    st.write(f'**Assunto:** {flashcard["Assunto"]}')

    card_content = flashcard["Frente"] if st.session_state.show_front else flashcard["Verso"]
    st.markdown(f'<div class="card-content">{card_content}</div>', unsafe_allow_html=True)

    # Botões centrais
    col_espaco_esquerda, col_central, col_espaco_direita = st.columns([1, 2, 1])

    with col_central:
        button_label = 'Virar' if st.session_state.show_front else 'Mostrar Frente'
        if st.button(button_label, key='flip_button', type='primary', use_container_width=True):
            st.session_state.show_front = not st.session_state.show_front
            st.rerun()

        st.markdown('<div class="button-spacing"></div>', unsafe_allow_html=True)

        if st.button('Voltar: INÍCIO !', use_container_width=True):
            del st.session_state.assunto
            del st.session_state.index
            del st.session_state.show_front
            st.rerun()

    # Lógica dos botões
    if st.session_state.get('anterior_btn'):
        st.session_state.index -= 1
        if st.session_state.index < 0:
            st.session_state.index = len(data) - 1
        st.session_state.show_front = True
        st.rerun()

    if st.session_state.get('proximo_btn'):
        st.session_state.index += 1
        if st.session_state.index >= len(data):
            st.session_state.index = 0
        st.session_state.show_front = True
        st.rerun()
