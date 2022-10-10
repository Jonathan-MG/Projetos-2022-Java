# Jonathan Martins Gomes - RA: 20.00862-7

class User():
    def __init__(self, name = "admin", email = None, password = "admin"):
        self._name = name
        self._email = email
        self._password = password
        self._contador = 0
    def get_Nome(self):
        return self._name
    def get_Email(self):
        return self._email
    def get_Senha(self):
        return self._password
    def set_Nome(self, name):
        if self._contador <= 2:
            self._contador += 1
            self._name = name
        else:
            return f'Número máximo de alterações atingido, não foi possível alterar o nome do usuário!'
    def set_Email(self, email):
        self._email = email
    def set_Senha(self, password):
        self._password = password
    def __str__(self) -> str:
        return f'User(name:{self._name}, email:{self._email}, password:{self._password})'
    