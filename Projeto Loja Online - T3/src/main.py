# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st
from models.product_model import Produto
from view.home_page import Home
from view.login import Login


produtos_db =  [Produto("God of War","Pow Pá Morre.",
                        "god_of_war",
                        200.00,
                        "./assets/Cover_God_of_War.jpg",
                        True),
                Produto("Spider-Man Remastered",
                        "Tchi Mari Jane.",
                        "spider_man",
                        350.00,
                        "./assets/Cover_Spider_Man.jpg",
                        True),
                Produto("Red Dead Redemption II",
                        "Tem sempre um trem Dutch.",
                        "red_dead_2",
                        75.00,
                        "./assets/Cover_Red_Dead_2.jpg",
                        True),
                Produto("Grand Theft Auto V",
                        "Lester the Molester.",
                        "gta_5",
                        75.00,
                        "./assets/Cover_GTA_V.jpg",
                        True),
                Produto("Final Fantasy VII Remake - Intergrade",
                        "Tifa.",
                        "ff7_remake",
                        250.00,
                        "./assets/Cover_FFVII.jpg",
                        True),
                Produto("Overwatch",
                        "Ixcurrega.",
                        "overwatch",
                        100.00,
                        "./assets/Cover_Overwatch.jpg",
                        True),
                Produto("Battlefield 2042",
                        "Todo bugado.",
                        "bf_2042",
                        125.00,
                        "./assets/Cover_Battlefield_2042.jpg",
                        True),
                Produto("Call of Duty MWII",
                        "Foge do Gás.",
                        "cod_mw2",
                        350.00,
                        "./assets/Cover_COD_MWII.jpg",
                        True),
                Produto("Cult of the Lamb",
                        "Jesus é uma ovelha.",
                        "cult_of_the_lamb",
                        100.00,
                        "./assets/Cover_Cult_of_the_Lamb.jpg",
                        True),
                ]

st.set_page_config(page_title="Snoteam",layout="centered",initial_sidebar_state="collapsed",menu_items=None)

if Login():
    Home(produtos_db)