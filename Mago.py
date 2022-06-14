from Jugador import *

class Mago(Jugador):
    def __init__(self, nombre, raza):
        super().__init__(nombre, raza)
    
    def bolaFuego(self):
        print(f"{self.nombre} a lanzado una bola de fuego")
    
    def escudoMagia(self):
        print(f"{self.nombre} se a lanzado un echizo de escudos sobre si mismo")


