import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Consulta de alunos",
    page_icon="📱"
)
st.title("Consulta de alunos")

st.divider( )
dados=pd.read_csv("Alunos.csv")
st.dataframe(dados)
st.image("Gilson_Mimi.jpg")
st.image("Gilson_Malu.jpg")
st.image("Lorraninha01.png")

