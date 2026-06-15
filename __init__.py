# Cenário: A - Locadora de veículos
# Aluno: Pedro Henrique da Silva Bispo

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .cliente_locadora import ClienteLocadora
from .veiculo import Veiculo
from .locacao import Locacao