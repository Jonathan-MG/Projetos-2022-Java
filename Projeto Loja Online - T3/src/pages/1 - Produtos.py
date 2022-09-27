import time
import streamlit as st

st.set_page_config(page_title="Home",layout="centered",initial_sidebar_state="collapsed",menu_items=None)
st.title("Produtos")

destaques,lancamentos,ofertas,perfil = st.tabs(["Destaques","Lançamentos","Ofertas","Perfil"])

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)