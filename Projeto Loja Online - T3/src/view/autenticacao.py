# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st
from controllers.user_controller import UserController
from controllers.login_controller import *
from controllers.cadastro_controller import *

# Retorna 'True' se o usuário/senha digitada estiver correto.
def Autenticar():
    def Teste_User():
        contador = 0
        while contador < st.session_state["users_db"].get_Quantidade_User():
            aux = st.session_state["users_db"].get_Users(contador)
            st.write(aux)
            contador += 1
    
    Autenticador = False    
    login,cadastro = st.tabs(["Login","Cadastre-se"])
    with login:
        Autenticador = Login()
    with cadastro:
        Cadastro()
        if st.button("Teste Users",key="Teste_U"):
            Teste_User()
    return Autenticador