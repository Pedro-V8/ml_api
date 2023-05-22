from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Manga(Base):
    __tablename__ = 'manga'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    img = Column(String(255), nullable=False)
    description = Column(String(500), nullable=False)
