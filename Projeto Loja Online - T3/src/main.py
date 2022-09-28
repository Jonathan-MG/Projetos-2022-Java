from models.products.item import Item
from models.cart.carrinho import Carrinho
import streamlit as st

if "carrinho" not in st.session_state:
    st.session_state["carrinho"] = Carrinho()
if "produtos" not in st.session_state:
    st.session_state["produtos"] =  [Item("God of War","Pow Pá Morre.","god_of_war",200.00,"./assets/Cover_God_of_War.jpg"),
                                     Item("Spider-Man Remastered","Tchi Mari Jane.","spider_man",350.00,"./assets/Cover_Spider_Man.jpg"),
                                     Item("Red Dead Redemption II","Tem sempre um trem Dutch.","red_dead_2",75.00,"./assets/Cover_Red_Dead_2.jpg"),
                                     Item("Grand Theft Auto V","Lester the Molester.","gta_5",75.00,"./assets/Cover_GTA_V.jpg"),
                                     Item("Final Fantasy VII Remake - Intergrade","Tifa.","ff7_remake",250.00,"./assets/Cover_FFVII.jpg"),
                                     Item("Overwatch","Ixcurrega.","overwatch",100.00,"./assets/Cover_Overwatch.jpg"),
                                     Item("Battlefield 2042","Todo bugado.","bf_2042",125.00,"./assets/Cover_Battlefield_2042.jpg"),
                                     Item("Call of Duty MWII","Foge do Gás.","cod_mw2",350.00,"./assets/Cover_COD_MWII.jpg"),
                                     Item("Cult of the Lamb","Jesus é uma ovelha.","cult_of_the_lamb",100.00,"./assets/Cover_Cult_of_the_Lamb.jpg"),]

st.set_page_config(page_title="Snoteam",layout="centered",initial_sidebar_state="collapsed",menu_items=None)

def check_password():
    # Retorna 'True' se o usuário/senha digitada estiver correto.
    
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

if check_password():
    store,cart = st.tabs(["Loja","Carrinho"])    
    with store:
        st.subheader("Destaques")
        c1,c2,c3 = st.columns(3,gap="small")
        c4,c5,c6 = st.columns(3,gap="small")
        c7,c8,c9 = st.columns(3,gap="small")
        colunas = [c1,c2,c3,c4,c5,c6,c7,c8,c9]
        var = 0
        for coluna in colunas:
            with coluna:
                st.image(st.session_state["produtos"][var].get_Imagem(), ("R$ "+ str(st.session_state["produtos"][var].get_Valor())))
                st.write("Descrição: "+st.session_state["produtos"][var].get_Descricao())
                if st.button("Adicionar ao carrinho", key = st.session_state["produtos"][var].get_Keyword()):
                    st.session_state["carrinho"].adicionar(st.session_state["produtos"][var])
                var += 1
    with cart:
        col1,col2,col3 = st.columns([1.5,5,2.5],gap = "small")
        with col1:
            st.write("Remover:")
            contador = 0
            while contador < st.session_state["carrinho"].get_Quantidade_Itens():
                aux = st.session_state["carrinho"].exibir_Itens(contador)
                if st.button("Remover",key = ("Remover_"+aux.get_Keyword()+str(contador))):
                    st.session_state["carrinho"].remover(aux)
                contador += 1        
        with col2:
            st.write("Itens:")
            i = 0
            while i < st.session_state["carrinho"].get_Quantidade_Itens():
                st.write(str(st.session_state["carrinho"].exibir_Itens(i)))
                i+=1
        with col3:
            st.write("Resumo da Compra:")
            st.write("Quantidade Total: "+str(st.session_state["carrinho"].get_Quantidade_Itens()))
            st.write("Valor total: R$ "+str(st.session_state["carrinho"].get_Valor_Total()))
            if st.button("Pagamento",key = ("pagamento")):
                st.write("Redirecionando...")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)