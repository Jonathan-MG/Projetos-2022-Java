from models.products.item import Item
from models.cart.carrinho import Carrinho
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
cart = Carrinho()


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
        c1,c2,c3 = st.columns(3,gap="small")
        c4,c5,c6 = st.columns(3,gap="small")
        c7,c8,c9 = st.columns(3,gap="small")
        colunas = [c1,c2,c3,c4,c5,c6,c7,c8,c9]
        var = 0
        prod_key_1 = "Produto_"
        for i in colunas:
            with i:
                prod_key_2 = str(var)
                prod_key = prod_key_1+prod_key_2
                st.image(produtos[var].get_Imagem(), produtos[var].get_Valor())
                if st.button("Adicionar ao carrinho", key=prod_key):
                    cart.adicionar(produtos[var])
                var += 1
        cart.adicionar(produtos[1])
        cart.adicionar(produtos[1])
        cart.adicionar(produtos[1])
        cart.adicionar(produtos[1])
    with carrinho:
        col1,col2 = st.columns([2,1],gap = "small")
        with col1:
            st.write("Itens:")
            i = 0
            while i < cart.get_Quantidade_Itens():
                st.write(str(cart.exibir_Itens(i)))
                i+=1
        with col2:
            st.write("Resumo da Compra:")
            st.write(str(cart.get_Quantidade_Itens()))
            st.write(str(cart.get_Valor_Total()))

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)