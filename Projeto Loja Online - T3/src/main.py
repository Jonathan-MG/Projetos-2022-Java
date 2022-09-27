from random import randint
from models.products.item import Item
import streamlit as st

produtos = [Item("God of War","Pow Pá Morre.",200.00,"./assets/Cover_God_of_War.jpg"),
            Item("Spider-Man","Tchi Mari Jane.",350.00,"./assets/Cover_Spider_Man.jpg"),
            Item("Red Dead Redemption II","Tem sempre um trem Dutch.",75.00,"./assets/Cover_Red_Dead_2.jpg"),
            Item("Grand Theft Auto V","Lester the Molester.",75.00,"./assets/Cover_GTA_V.jpg"),
            Item("Final Fantasy VII Remake - Intergrade","Tifa.",250.00,"./assets/Cover_FFVII.jpg"),
            Item("Overwatch","Ixcurrega.",100.00,"./assets/Cover_Overwatch.jpg"),
            Item("Battlefield 2042","Todo bugado.",125.00,"./assets/Cover_Battlefield_2042.jpg"),
            Item("Call of Duty MWII","Foge do Gás.",350.00,"./assets/Cover_COD_MWII.jpg"),
            Item("Cult of the Lamb","Jesus é uma ovelha.",100.00,"./assets/Cover_Cult_of_the_Lamb.jpg"),]

st.set_page_config(page_title="Snoteam",layout="centered",initial_sidebar_state="collapsed",menu_items=None)

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
        st.error("Usuário/senha incorreto.")
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
            st.image("./assets/Cover_COD_MWII.jpg",caption="R$ 350,00")
            if st.button(label="Adicionar ao carrinho!",key=randint(0,10000)):
                st.write("Redirecionando...")
        with col2:
            st.image("./assets/Cover_Battlefield_2042.jpg",caption="R$ 125,00")
            if st.button(label="Adicionar ao carrinho!",key=randint(0,10000)):
                st.write("Redirecionando...")
        with col3:
            st.image("./assets/Cover_Cult_of_the_Lamb.jpg",caption="R$ 100,00")
            if st.button(label="Adicionar ao carrinho!",key=randint(0,10000)):
                st.write("Redirecionando...")
        col4,col5,col6 = st.columns(3,gap = "small")
        with col4:
            st.image("./assets/Cover_Red_Dead_2.jpg",caption="R$ 75,00")
            if st.button(label="Adicionar ao carrinho!",key=randint(0,10000)):
                st.write("Redirecionando...")
        with col5:
            st.image("./assets/Cover_GTA_V.jpg",caption="R$ 75,00")
            if st.button(label="Adicionar ao carrinho!",key=randint(0,10000)):
                st.write("Redirecionando...")
        with col6:
            st.image("./assets/Cover_God_of_War.jpg",caption="R$ 200,00")
            if st.button(label="Adicionar ao carrinho!",key=randint(0,10000)):
                st.write("Redirecionando...")
        col7,col8,col9 = st.columns(3,gap = "small")
        with col7:
            st.image("./assets/Cover_FFVII.jpg",caption="R$ 250,00")
            if st.button(label="Adicionar ao carrinho!",key=randint(0,10000)):
                st.write("Redirecionando...")
        with col8:
            st.image("./assets/Cover_Spider_Man.jpg",caption="R$ 350,00")
            if st.button(label="Adicionar ao carrinho!",key=randint(0,10000)):
                st.write("Redirecionando...")
        with col9:
            st.image("./assets/Cover_Overwatch.jpg",caption="R$ 100,00")
            if st.button(label="Adicionar ao carrinho!",key=randint(0,10000)):
                st.write("Redirecionando...")
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