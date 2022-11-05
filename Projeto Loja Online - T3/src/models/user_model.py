# Jonathan Martins Gomes - RA: 20.00862-7

class User():
    def __init__(self, username = "admin", email = None, password = "admin", cpf = None, birthdate = None, name = "Admin"):
        self._username = username
        self._email = email
        self._password = password
        self._cpf = cpf
        self._birthdate = birthdate
        self._name = name
        self._contador = 0
    def get_Username(self):
        return self._username
    def get_Email(self):
        return self._email
    def get_Senha(self):
        return self._password
    def get_cpf(self):
        return self._cpf
    def get_birthdate(self):
        return self._birthdate
    def get_Name(self):
        return self._name
    def set_Username(self, username):
        if self._contador <= 2:
            self._contador += 1
            self._username = username
        else:
            return f'Número máximo de alterações atingido, não foi possível alterar o nome do usuário!'
    def set_Email(self, email):
        self._email = email
    def set_Senha(self, password):
        self._password = password
    def set_cpf(self, cpf):
        self._cpf = cpf
    def set_birthdate(self, birthdate):
        self._birthdate = birthdate
    def set_Name(self, name):
        self._name = name
    def __str__(self) -> str:
        return f'User(Name:{self._name}, Birthdate:{self._birthdate}, CPF:{self._cpf} ,Username:{self._username}, Email:{self._email}, Password:{self._password})'
    