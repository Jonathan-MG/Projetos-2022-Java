# Jonathan Martins Gomes - RA: 20.00862-7

from controllers.user_controller import UserController
from view.login import *
from view.loja import *

users_db = UserController()
if check_password():
    Loja()