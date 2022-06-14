from Jugador import *

class Caballero(Jugador):
    def __init__(self, nombre, raza):
        super().__init__(nombre, raza)
    
    def ataqueEspada(self):
        print(f"Ataque de espada")
    
    def usarEscudo(self):
        print(f"Usuario a utilizado el escudo")

