# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st
from view.login import Teste_User

class Profile_Ctrl:
    def __init__(self) -> None:
        #current_user = (f'{st.session_state["username"]}')
        current_user = st.text_input("Digite o Usuário para realizar a alteração:",key="id_user")
        new_user_email = st.text_input("Digite o novo endereço de email:",key="new_user_email")
        if st.button("Alterar E-mail",key="change_email_button"):
            st.session_state["users_db"].get_Users(current_user).set_Email(new_user_email)                
        new_user_password = st.text_input("Digite uma nova senha:",key="new_user_password")
        if st.button("Alterar Senha",key="change_password_button"):
            st.session_state["users_db"].get_Users(current_user).set_Senha(new_user_password)
        if st.button("Teste Users",key="Teste_U2"):
            Teste_User() 