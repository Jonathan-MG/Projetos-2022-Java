# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st
from controllers.product_controller import Product_Controller
from controllers.carrinho import Carrinho
from controllers.store_controller import Store_Ctrl
from controllers.cart_controller import Cart_Ctrl
from controllers.profile_controller import Profile_Ctrl
from controllers.admin_controller import Admin_Ctrl

class Home:
    def __init__(self,produtos_db):
        if "carrinho" not in st.session_state:
            st.session_state["carrinho"] = Carrinho()
        st.session_state["produtos"] = Product_Controller()
        
        for produto in produtos_db:
            st.session_state["produtos"].adicionar_a_lista(produto)
        
        store,cart,profile,administration = st.tabs(["Loja","Carrinho","Perfil","Novos Produtos"])    
        with store:
            Store_Ctrl()
        with cart:
            Cart_Ctrl()
        with profile:
            Profile_Ctrl()
        with administration:
            Admin_Ctrl()
        
        hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
        st.markdown(hide_menu_style, unsafe_allow_html=True)