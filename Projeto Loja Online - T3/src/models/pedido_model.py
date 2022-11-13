# Jonathan Martins Gomes - RA: 20.00862-7

class Pedido:
    def __init__(self, numero_pedido, id_cliente, carrinho, data_hora) -> None:
        self.numero_pedido = numero_pedido
        self.id_cliente = id_cliente
        self.carrinho = carrinho
        self.data_hora = data_hora

    def __str__(self) -> str:
        return f"""Número do Pedido: {self.numero_pedido} - Cliente: {self.id_cliente} - Data: {self.data_hora}:
                   Carrinho: {self.carrinho} """