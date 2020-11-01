from diccionario import Word
from base import Session,engine,Base

Base.metadata.create_all(engine)

session = Session()

#Palabras

w1 = Word(1, "Que Xopa", "Saludar")
w2 = Word(2, "Chantin", "Casa")
w3 = Word(3, "Nave", "Carro")
w4 = Word(4, "Parking", "Fiesta")
w5 = Word(5, "Fren", "Amigo")

session.add(w1)
session.add(w2)
session.add(w3)
session.add(w4)
session.add(w5)

session.commit()
session.close()