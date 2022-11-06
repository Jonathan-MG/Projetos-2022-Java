# Jonathan Martins Gomes - RA: 20.00862-7
from models.user_model import User
import os
        
def update_user_db(user_db):
    for user in user_db:
        username = user.get_Username()
        user_password = user.get_Senha()
        user_str = f'{username} = "{user_password}"'
        if os.path.exists(".streamlit/secrets.toml"):
            user_db = open(".streamlit/secrets.toml",'r')
            users_db_read = user_db.read()
            user_db.close()
            if f'{username} =' in users_db_read:
                print(f'Nome de usuário:{username} já está em uso!')
            else:
                user_db = open(".streamlit/secrets.toml",'a')
                user_db.write(f'\n{user_str}')
                user_db.close()
        else:
            user_db = open(".streamlit/secrets.toml",'a')
            user_db.write("[passwords]")
            user_db.write(f'\n{user_str}')
            user_db.close()

class UserController():
    def __init__(self) -> None:
        self._users = [User()]
        update_user_db(self._users)
    
    def add_user(self, username, email, password, cpf, birthdate, name):
        Aux = User(username, email, password, cpf, birthdate, name)
        self._users.append(Aux)
        update_user_db(self._users)
    
    def get_Users(self,user):
        return self._users[user]
    
    def get_Quantidade_User(self):
        return len(self._users)
    
    def checkUser(self, user):
        return user in self._users
    
    def checkLogin(self, username, password, email):
        user_teste = User(username = username, password = password, email = email)
        for user in self._users:
            if user._username == user_teste._username and user._password == user_teste._password and user._email == user_teste._email:
                return True
        return False

