from datetime import datetime

from pytz import timezone
from sqlalchemy import Column, DateTime, Integer, String

from db import Base


class Pokemon(Base):
    __tablename__ = "pokemon"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    tipo = Column(String)
    criado_em = Column(
        DateTime, default=lambda: datetime.now(timezone("America/Sao_Paulo"))
    )
