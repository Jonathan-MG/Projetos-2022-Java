# Jonathan Martins Gomes - RA: 20.00862-7
from models.product_model import Produto

class Product_Controller():
    def __init__(self) -> None:
        self._lista_de_produtos = []
    # Demais métodos da classe
    def adicionar_a_lista(self,produto):
        self._lista_de_produtos.append(produto)
    def criar_novo_produto(self,nome,descricao,keyword,valor,imagem):
        Aux = Produto(nome,descricao,keyword,valor,imagem)  
        self._lista_de_produtos.append(Aux) 
    def exibir_Produtos(self,produto):
        return self._lista_de_produtos[produto]
    def get_Produto(self,index):
        return self._lista_de_produtos[index]
    def get_Quantidade_Produtos(self):
        return len(self._lista_de_produtos)
    def remover(self,produto):
        if produto in self._lista_de_produtos:
            self._lista_de_produtos.remove(produto)