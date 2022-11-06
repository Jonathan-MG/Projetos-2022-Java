# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st

def Cadastro():
    def Confirma_cadastro():
        # if not st.session_state["users_db"].checkLogin(new_user,
        #                                                 new_userpassword,
        #                                                 new_useremail):
        st.session_state["users_db"].add_user(new_user,
                                              new_useremail,
                                              new_userpassword,
                                              new_usercpf,
                                              new_userbirth,
                                              new_username)
        st.write("Cadastro realizado com sucesso!")
    
    new_username = st.text_input(label="Digite seu nome:", key="new_username")
    new_userbirth = st.text_input(label="Digite sua data de nascimento:", key="new_userbirth")
    new_usercpf = st.text_input(label="Digite seu CPF (Apenas números):", key="new_usercpf")
    new_user = st.text_input(label="Digite seu nome de usuário desejado:", key="new_user")
    new_useremail = st.text_input(label="Digite seu E-mail:", key="new_useremail")
    new_userpassword = st.text_input(label="Digite a senha desejada:", key="new_userpassword")
    if st.button("Cadastrar", key="botao_cadastro"):
        Confirma_cadastro()