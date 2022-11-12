# Jonathan Martins Gomes - RA: 20.00862-7
from models.product_model import Produto
from dao.produto_dao import Produto_DAO
import base64

class Product_Ctrl():
    def __init__(self) -> None:
        self.product_db = Produto_DAO()
        self._lista_de_produtos = self.product_db.get_all()
    
    # Demais métodos da classe
    def adicionar_a_lista(self,produto):
        if produto not in self._lista_de_produtos:
            self._lista_de_produtos.append(produto)
    
    def criar_novo_produto(self,nome,descricao,keyword,valor,imagem):
        bin_string = base64.b64encode(imagem.getvalue())
        construct_img = base64.b64decode((bin_string))
        Aux = Produto(nome,descricao,keyword,valor,construct_img)  
        self.product_db.inserir_item(Aux) 
    
    def exibir_Produtos(self,produto):
        return self._lista_de_produtos[produto]
    
    def get_Produto(self,index):
        return self._lista_de_produtos[index]
    
    def get_Quantidade_Produtos(self):
        return len(self._lista_de_produtos)
    
    def remover(self,produto):
        return self.product_db.deletar_item(produto)