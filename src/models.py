from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from db import Base


class Pokemon(Base):
    __tablename__ = "pokemon"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    tipo = Column(String)
    criado_em = Column(DateTime, default=func.now())
