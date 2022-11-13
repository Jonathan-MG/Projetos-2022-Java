# Jonathan Martins Gomes
# from controllers.carrinho_controller import Carrinho_Ctrl
from models.pedido_model import Pedido
from dao.pedido_dao import PedidoDAO

class Pedido_Ctrl:
    def __init__(self) -> None:
        self.pedido_db = PedidoDAO()

    def inserir_pedido(self,id_cliente,carrinho,data_hora):
        numero_pedido = len(self.pedido_db.get_all())+1
        Aux = Pedido(numero_pedido,id_cliente,carrinho,data_hora)
        self.pedido_db.inserir_pedido(Aux)