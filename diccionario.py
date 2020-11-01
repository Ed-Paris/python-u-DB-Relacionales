from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import relationship
from base import Base

class Word(Base):
    __tablename__ = 'Diccionario'

    id = Column(Integer,primary_key=True)
    palabra = Column(String)
    significado = Column(String)

    def __init__(self, id, palabra, significado):

        self.id = id
        self.palabra = palabra
        self.significado = significado
