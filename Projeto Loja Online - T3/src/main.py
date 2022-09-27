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
        col1,col2,col3 = st.columns(3,gap = "small")
        with col1:
            st.image("./assets/Cover_COD_MWII.jpg")
        
        with col2:
            st.image("./assets/Cover_Battlefield_2042.jpg")
        
        with col3:
            st.image("./assets/Cover_Cult_of_the_Lamb.jpg")
        
        st.subheader("Ofertas")
        col4,col5,col6 = st.columns(3,gap = "small")
        with col4:
            st.image("./assets/Cover_Red_Dead_2.jpg")
        
        with col5:
            st.image("./assets/Cover_GTA_V.jpg")
        
        with col6:
            st.image("./assets/Cover_God_of_War.jpg")
        
        st.subheader("Pre-Order")
        col7,col8,col9 = st.columns(3,gap = "small")
        with col7:
            st.image("./assets/Cover_FFVII.jpg")
        
        with col8:
            st.image("./assets/Cover_Spider_Man.jpg")
        
        with col9:
            st.image("./assets/Cover_Overwatch.jpg")
    
    with carrinho:
        col1,col2 = st.columns([3,1],gap = "small")
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