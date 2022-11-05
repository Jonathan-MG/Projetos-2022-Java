# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st
from controllers.user_controller import UserController

def Cadastro():
    new_username = st.text_input(label="Digite seu nome:", key="new_username",on_change=None)
    new_userbirth = st.text_input(label="Digite sua data de nascimento:", key="new_userbirth",on_change=None)
    new_usercpf = st.text_input(label="Digite seu CPF (Apenas números):", key="new_usercpf",on_change=None)
    new_user = st.text_input(label="Digite seu nome de usuário desejado:", key="new_user",on_change=None)
    new_useremail = st.text_input(label="Digite seu E-mail:", key="new_useremail",on_change=None)
    new_userpassword = st.text_input(label="Digite a senha desejada:", key="new_userpassword",on_change=None)
    if st.button("Cadastrar", key="botao_cadastro"):
        st.session_state["users_db"].add_user(new_user,new_useremail,new_userpassword,new_usercpf,new_userbirth,new_username)
        return True
