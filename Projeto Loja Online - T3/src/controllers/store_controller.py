# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st

class Store_Ctrl:
    # def Criar_Coluna(quant_itens):
    #     n_linhas = quant_itens//3
    #     if (quant_itens % 3) != 0:
    #         n_linhas += 1 
    #     pass
    
    def __init__(self) -> None:
        st.subheader("Destaques")
        c1,c2,c3 = st.columns(3,gap="small")
        c4,c5,c6 = st.columns(3,gap="small")
        c7,c8,c9 = st.columns(3,gap="small")
        c10,c11,c12 = st.columns(3,gap="small")
        colunas = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12]
        
        if "colunas_aux" not in st.session_state:
            st.session_state["colunas_aux"] = 0
            
        quant_produtos = 0
        quant_produtos = st.session_state["produtos"].get_Quantidade_Produtos()
        
        for st.session_state["colunas_aux"] in range(quant_produtos):
            print(f'Coluna: {st.session_state["colunas_aux"]}')
            print(f'Quant.: {quant_produtos}')
            with colunas[st.session_state["colunas_aux"]]:
                st.image(st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]).get_Imagem(), st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]).get_Descricao())
                st.write("R$ "+ str(st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]).get_Valor()))
                if st.button("Adicionar ao carrinho", key = st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]).get_Keyword()+str(st.session_state["colunas_aux"])):
                    st.session_state["carrinho"].adicionar(st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]))
                    st.write("Produto adicionado ao carrinho!")
                
            
        # for coluna in colunas:
        #     with coluna:
        #         print(f'Coluna: {st.session_state["colunas_aux"]}')
        #         print(f'Quant.: {quant_produtos}')
        #         if st.session_state["colunas_aux"] < quant_produtos:
        #             st.image(st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]).get_Imagem(), st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]).get_Descricao())
        #             st.write("R$ "+ str(st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]).get_Valor()))
        #             if st.button("Adicionar ao carrinho", key = st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]).get_Keyword()):
        #                 st.session_state["carrinho"].adicionar(st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]))
        #                 st.write("Produto adicionado ao carrinho!")
        #     st.session_state["colunas_aux"] += 1                    
        #     if (st.session_state["colunas_aux"] > quant_produtos):
        #         st.session_state["colunas_aux"] = quant_produtos
                
