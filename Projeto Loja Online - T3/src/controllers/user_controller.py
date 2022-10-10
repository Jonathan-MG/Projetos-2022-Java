from models.users.users import User
import os

def update_user_db(self,user):
    if os.path.exists(".streamlit/secrets.toml"):
        user_db = open(".streamlit/secrets.toml",'a')
        user_db.write(f'{user.get_Nome()}="{user.get_Senha()}"')
        user_db.close()
    else:
        user_db = open(".streamlit/secrets.toml",'a')
        user_db.write("[passwords]")
        user_db.write(f'{user.get_Nome()}="{user.get_Senha()}"')
        user_db.close()

class UserController():
    def __init__(self) -> None:
        self._users = [User(name = "admin",email = "admin",password = "admin")]
        update_user_db(self._users[0])
    def add_user(self, name, email, password):
        Aux = User(name, email, password)
        self._users.append(Aux)
    def checkUser(self, user):
        return user in self.users
    def checkLogin(self, name, password):
        user_teste = User(name = name, password = password, email = None)
        for user in self._users:
            if user._name == user_teste._name and user._password == user_teste._password:
                return True
        return False