# from dao.produto_dao import Produto_DAO
# from models.product_model import Produto
# from models.user_model import User
# from dao.user_dao import User_DAO




# user_db = User_DAO()
# aux = User("admin","admin","admin",None,None,"admin")
# user_db.inserir_usuario(aux)

# db = Produto_DAO()
# produtos_db =  [Produto("God of War","Pow Pá Morre.",
#                         "god_of_war",
#                         200.00,
#                         "./assets/Cover_God_of_War.jpg",
#                         True),
#                 Produto("Spider-Man Remastered",
#                         "Tchi Mari Jane.",
#                         "spider_man",
#                         350.00,
#                         "./assets/Cover_Spider_Man.jpg",
#                         True),
#                 Produto("Red Dead Redemption II",
#                         "Tem sempre um trem Dutch.",
#                         "red_dead_2",
#                         75.00,
#                         "./assets/Cover_Red_Dead_2.jpg",
#                         True),
#                 Produto("Grand Theft Auto V",
#                         "Lester the Molester.",
#                         "gta_5",
#                         75.00,
#                         "./assets/Cover_GTA_V.jpg",
#                         True),
#                 Produto("Final Fantasy VII Remake - Intergrade",
#                         "Tifa.",
#                         "ff7_remake",
#                         250.00,
#                         "./assets/Cover_FFVII.jpg",
#                         True),
#                 Produto("Overwatch",
#                         "Ixcurrega.",
#                         "overwatch",
#                         100.00,
#                         "./assets/Cover_Overwatch.jpg",
#                         True),
#                 Produto("Battlefield 2042",
#                         "Todo bugado.",
#                         "bf_2042",
#                         125.00,
#                         "./assets/Cover_Battlefield_2042.jpg",
#                         True),
#                 Produto("Call of Duty MWII",
#                         "Foge do Gás.",
#                         "cod_mw2",
#                         350.00,
#                         "./assets/Cover_COD_MWII.jpg",
#                         True),
#                 Produto("Cult of the Lamb",
#                         "Jesus é uma ovelha.",
#                         "cult_of_the_lamb",
#                         100.00,
#                         "./assets/Cover_Cult_of_the_Lamb.jpg",
#                         True)]
# for produto in produtos_db:
#     db.inserir_item(produto)
# produtos_db = db.get_all()
# for produto in produtos_db:
#         print(produto)
#         decodeit = open(f'./teste_img/{produto.get_Nome()}.jpeg', 'wb')
#         decodeit.write(produto.get_Imagem())
#         decodeit.close()