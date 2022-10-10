# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st
from controllers.user_controller import UserController

# Retorna 'True' se o usuário/senha digitada estiver correto.
def Login():
    st.set_page_config(page_title="Snoteam",layout="centered",initial_sidebar_state="collapsed",menu_items=None)
    if "users_db" not in st.session_state:
        st.session_state["users_db"] = UserController()
    def password_entered():
        # Checa se o usuário/senha digitado está correto.
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            # Apaga a senha usada da session_state atual.
            del st.session_state["password"]  
            # del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False
    if "password_correct" not in st.session_state:
        # Inicialização, exibe o local para digitação de usuário e senha.
        st.text_input(label="Digite seu E-mail:", key="username")
        st.text_input(label="Digite sua Senha:", type="password", key="password")
        col1,col2 = st.columns(spec=[1,10],gap="small")
        with col1:    
            if st.button(label="Login"):
                password_entered()
        with col2:
            if st.button(label="Esqueci a senha"):
                st.write("Redirecionando...")
        return False
    elif not st.session_state["password_correct"]:
        # Senha incorreta - exibe mensagem de erro e permite digitar novamente.
        st.text_input(label="Digite seu E-mail:", key="username")
        st.text_input(label="Digite sua Senha:", type="password", key="password")
        col1,col2 = st.columns(spec=[1,10],gap="small")
        with col1:    
            if st.button(label="Login"):
                password_entered()
        with col2:
            if st.button(label="Esqueci a senha"):
                st.write("Redirecionando...")
        st.error("Usuário/senha incorreto.")
        return False
    else:
        # Se a sennha for correta.
        return True