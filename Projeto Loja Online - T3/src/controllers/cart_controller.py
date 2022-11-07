# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st

class Cart_Ctrl:
    def __init__(self) -> None:
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