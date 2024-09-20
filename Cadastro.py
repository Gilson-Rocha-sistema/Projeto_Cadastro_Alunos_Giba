import streamlit as st
import pandas as pd
from datetime import date
st.set_page_config(
    page_title="Cadastro de alunos",
    page_icon="📱"
)
st.title("Cadastro de alunos")

st.divider( )

def Gravar_dados(nome, data_nasc, tipo):
    if nome and data_nasc <= date.today():
        with open("Alunos.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{data_nasc}, {tipo}\n")    

        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False


nome = st.text_input("Digite o nome do aluno",
                     key="nome_aluno")
dt_nasc = st.date_input("Data de nascimeto",
                        format="DD/MM/YYYY")
tipo = st.selectbox("Tipo de pessoa",
                    ["Jurídica", "Física"])

btn_cadastrar = st.button("Cadastrar", on_click=Gravar_dados,
                          args=[nome, dt_nasc, tipo])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Aluno cadastrado com sucesso", icon="✅")
    else:
        st.error("Houve algum problema no cadastro", icon="❌")  


