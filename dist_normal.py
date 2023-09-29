import streamlit as st
import pandas as pd
import plotly.express as px
from scipy import stats

# Título do aplicativo
st.title("Teste de Normalidade e Histograma")

# Carregando o arquivo Excel
uploaded_file = st.file_uploader("Faça upload de um arquivo Excel", type=["xls", "xlsx"])

if uploaded_file is not None:
    # Lendo o arquivo Excel em um DataFrame do Pandas
    df = pd.read_excel(uploaded_file)

    # Selecionando a coluna para análise
    selected_column = st.selectbox("Selecione a coluna para análise", df.columns)

    # Realizando o teste de normalidade (Shapiro-Wilk)
    st.subheader("Resultado do Teste de Normalidade (Shapiro-Wilk)")
    _, p_value = stats.shapiro(df[selected_column])

    if p_value > 0.05:
        st.write(f"A distribuição parece ser normal (p-valor = {p_value:.4f} > 0.05).")
    else:
        st.write(f"A distribuição não parece ser normal (p-valor = {p_value:.4f} <= 0.05).")

    # Exibindo um histograma interativo da coluna selecionada usando Plotly
    st.subheader("Histograma da Coluna selecionada")
    fig = px.histogram(df, x=selected_column, title=f'Histograma de {selected_column}')
    st.plotly_chart(fig)
