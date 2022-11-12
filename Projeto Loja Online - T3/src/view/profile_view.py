# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st
# from view.login import Teste_User

class Profile_View:
    def __init__(self) -> None:
        if "userlogged" not in st.session_state:
            st.session_state["userlogged"] = st.session_state["username"]
        current_user = (f'{st.session_state["userlogged"]}')
        
        new_user_email = st.text_input("Digite o novo endereço de email:",key="new_user_email")
        if st.button("Alterar E-mail",key="change_email_button"):
            st.session_state["users_db"].get_User(current_user).set_Email(new_user_email)
            st.write("Troca de e-mail realizada com sucesso!")                
        
        new_user_password = st.text_input("Digite uma nova senha:",key="new_user_password")
        if st.button("Alterar Senha",key="change_password_button"):
            st.session_state["users_db"].get_User(current_user).set_Senha(new_user_password)
            st.write("Troca de senha realizada com sucesso!")
        # if st.button("Teste Users",key="Teste_U2"):
        #     Teste_User() 