# Cenário: A - Locadora de veículos
# Aluno: Pedro Henrique da Silva Bispo

from . import db
from .base import ModeloBase


class ClienteLocadora(ModeloBase):
    __tablename__ = "clientes_locadora"

    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), nullable=False, unique=True)

    locacoes = db.relationship(
        "Locacao",
        back_populates="cliente"
    )