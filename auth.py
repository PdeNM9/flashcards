import pandas as pd
import streamlit as st


def load_data():
    try:
        url = 'https://docs.google.com/spreadsheets/d/1TOTY7grKG5P6uoSIUc0qk5BBT_Fo7t4vpAYW43NlzyI/export?format=csv&gid=0'

        data = pd.read_csv(url)

        if data.empty:
            st.error('Nenhum dado encontrado.')
            return pd.DataFrame()
        else:
            return data
    except Exception as e:
        st.error(f'Erro ao carregar os dados: {str(e)}')
        return pd.DataFrame()
