from Jugador import *

class Barbaro(Jugador):
    def __init__(self, nombre, raza):
        super().__init__(nombre, raza)
    
    def ataqueHacha(self):
        print(f"{self.nombre} a lanzado hachas hacia el enemigo")
    
    def escudoBarbaro(self):
        print(f"{self.nombre} a utilizado su escudo")
