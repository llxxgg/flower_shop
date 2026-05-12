from sqlalchemy import Column, BigInteger, String, DECIMAL, Text, DateTime
from sqlalchemy.sql import func
from ..database import Base


class Flower(Base):
    __tablename__ = "flowers"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    image = Column(String(500), nullable=True)
    description = Column(Text, nullable=True)
    category = Column(String(50), nullable=True, index=True)
    create_time = Column(DateTime, server_default=func.now(), nullable=False)
