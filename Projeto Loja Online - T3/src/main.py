import time
import streamlit as st

st.set_page_config(page_title="Snoteam",layout="wide",initial_sidebar_state="collapsed",menu_items=None)

def check_password():
    """Returns `True` if the user had a correct password."""
    
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
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
        # Password not correct, show input + error.
        st.text_input(label="Digite seu E-mail:", key="username")
        st.text_input(label="Digite sua Senha:", type="password", key="password")
        col1,col2 = st.columns(spec=[1,10],gap="small")
        with col1:    
            if st.button(label="Login"):
                password_entered()
        with col2:
            if st.button(label="Esqueci a senha"):
                st.write("Redirecionando...")
        st.error("😕 User not known or password incorrect")
        return False
    
    else:
        # Password correct.
        return True

if check_password():
    loja,carrinho = st.tabs(["Loja","Carrinho"])
    
    with loja:
        st.subheader("Destaques")
        col1,col2,col3 = st.columns(3)
        with col1:
            st.write("1")
        
        with col2:
            st.write("2")
        
        with col3:
            st.write("3")
        
        st.subheader("Ofertas")
        col4,col5,col6 = st.columns(3)
        with col4:
            st.write("1")
        
        with col5:
            st.write("2")
        
        with col6:
            st.write("3")
        
        st.subheader("Pre-Order")
        col7,col8,col9 = st.columns(3)
        with col7:
            st.write("1")
        
        with col8:
            st.write("2")
        
        with col9:
            st.write("3")
    
    with carrinho:
        col1,col2 = st.columns([3,1])
        with col1:
            st.write("Itens")
        
        with col2:
            st.write("Resumo da Compra:")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)