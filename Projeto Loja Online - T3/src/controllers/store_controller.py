# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st

class Store_Ctrl:
    def __init__(self) -> None:
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
