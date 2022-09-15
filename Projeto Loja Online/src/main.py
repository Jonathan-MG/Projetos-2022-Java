import streamlit as st

main, profile, cart = st.tabs(["Loja","Perfil","Carrinho"]) 

with main:
    st.title("Página da loja")

with profile:
    st.title("Página de perfis")

with cart:
    st.title("Página do carrinho")

st.sidebar.title("Tabs")