# Jonathan Martins Gomes - RA: 20.00862-7
import base64

def Img_Conversor(caminho_img):
    with open(caminho_img, "rb") as image2string:
        string_img = base64.b64encode(image2string.read())
    image2string.close()
    return string_img

class Produto():    
    # Método construtor
    def __init__(self,nome,descricao,keyword,valor,imagem,ispath = False):
        self._nome = nome
        self._descricao = descricao
        self._keyword = keyword
        self._valor = valor
        # CORRIGIR DEPOIS DE IMPLEMENTAR O BANCO DE DADOS
        if ispath == True:
            self._imagem = Img_Conversor(imagem)
        else:
            self._imagem = imagem
    # Getters da classe
    def get_Nome(self):
        return self._nome
    
    def get_Descricao(self):
        return self._descricao
    
    def get_Keyword(self):
        return self._keyword
    
    def get_Valor(self):
        return self._valor
    
    def get_Imagem(self):
        img_convertida = base64.b64decode(self._imagem)
        return img_convertida
    
    # Faz com que o item print de forma especifica
    def __str__(self) -> str:
        return f'Nome: {self._nome} - R$ {str(self._valor)}'