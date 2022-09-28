class Item():
    # Método construtor
    def __init__(self,nome,descricao,valor,imagem):
        self._nome = nome
        self._descricao = descricao
        self._valor = valor
        self._imagem = imagem
    # Getters da classe
    def get_Nome(self):
        return self._nome
    def get_Descricao(self):
        return self._descricao
    def get_Valor(self):
        return self._valor
    def get_Imagem(self):
        return self._imagem
    # Faz com que o item print de forma especifica
    def __str__(self) -> str:
        return self._nome + " - R$ "+ str(self._valor)
    # Compara itens
    def __eq__(self, __o: object) -> bool:
        if(isinstance(__o,Item)):
            return self._nome == __o.get_Nome()
        return False