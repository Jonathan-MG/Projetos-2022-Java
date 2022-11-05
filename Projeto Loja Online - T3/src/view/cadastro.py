# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st
from controllers.user_controller import UserController

class Cadastro():
    def __init__(self, user_db) -> None:
        user_db = UserController()
        new_username = st.text_input(label="Digite seu nome:", key="new_username")
        new_userbirth = st.text_input(label="Digite sua data de nascimento:", key="new_userbirth")
        new_usercpf = st.text_input(label="Digite seu CPF (Apenas números):", key="new_usercpf")
        new_user = st.text_input(label="Digite seu nome de usuário desejado:", key="new_user")
        new_useremail = st.text_input(label="Digite seu E-mail:", key="new_useremail")
        new_userpassword = st.text_input(label="Digite a senha desejada:", key="new_userpassword")

    