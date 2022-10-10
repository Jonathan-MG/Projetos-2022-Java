# Jonathan Martins Gomes - RA: 20.00862-7
from controllers.product_controller import Product_Controller
from controllers.carrinho import Carrinho
import streamlit as st

class Loja:
    def __init__(self,produtos_db):
        if "carrinho" not in st.session_state:
            st.session_state["carrinho"] = Carrinho()
        if "produtos" not in st.session_state:
            st.session_state["produtos"] = Product_Controller()
        for produto in produtos_db:
            st.session_state["produtos"].adicionar_a_lista(produto)
        
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
                    st.image(st.session_state["produtos"].get_Produto(var).get_Imagem(), st.session_state["produtos"].get_Produto(var).get_Descricao())
                    st.write("R$ "+ str(st.session_state["produtos"].get_Produto(var).get_Valor()))
                    if st.button("Adicionar ao carrinho", key = st.session_state["produtos"].get_Produto(var).get_Keyword()):
                        st.session_state["carrinho"].adicionar(st.session_state["produtos"].get_Produto(var))
                        st.write("Produto adicionado ao carrinho!")
                    var += 1        
        with cart:
            col1,col2,col3 = st.columns([1.5,5,2.5],gap = "small")
            with col1:
                st.write("Remover:")
                contador = 0
                while contador < st.session_state["carrinho"].get_Quantidade_Produtos():
                    aux = st.session_state["carrinho"].exibir_Produtos(contador)
                    if st.button("Remover",key = ("Remover_"+aux.get_Keyword()+str(contador))):
                        st.session_state["carrinho"].remover(aux)
                    contador += 1        
            with col2:
                st.write("Produtos:")
                i = 0
                while i < st.session_state["carrinho"].get_Quantidade_Produtos():
                    st.write(str(st.session_state["carrinho"].exibir_Produtos(i)))
                    st.text(" ")
                    i+=1
            with col3:
                st.write("Resumo da Compra:")
                st.write("Quant. de Produtos: "+str(st.session_state["carrinho"].get_Quantidade_Produtos()))
                st.write("Valor total: R$ "+str(st.session_state["carrinho"].get_Valor_Total()))
                if st.button("Pagamento",key = ("pagamento")):
                    st.write("Redirecionando...")
        
        hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
        st.markdown(hide_menu_style, unsafe_allow_html=True)