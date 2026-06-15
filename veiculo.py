# Cenário: A - Locadora de veículos
# Aluno: Pedro Henrique da Silva Bispo

from . import db
from .base import ModeloBase


class Veiculo(ModeloBase):
    __tablename__ = "veiculos"

    modelo = db.Column(db.String(100), nullable=False)
    placa = db.Column(db.String(10), nullable=False, unique=True)

    locacoes = db.relationship(
        "Locacao",
        back_populates="veiculo"
    )