# Cenário: A - Locadora de veículos
# Aluno: Pedro Henrique da Silva Bispo

from datetime import datetime

from . import db
from .base import ModeloBase


class Locacao(ModeloBase):
    __tablename__ = "locacoes"

    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey("clientes_locadora.id"),
        nullable=False
    )

    veiculo_id = db.Column(
        db.Integer,
        db.ForeignKey("veiculos.id"),
        nullable=False
    )

    data_inicio = db.Column(
        db.DateTime,
        default=datetime.now,
        nullable=False
    )

    cliente = db.relationship(
        "ClienteLocadora",
        back_populates="locacoes"
    )

    veiculo = db.relationship(
        "Veiculo",
        back_populates="locacoes"
    )