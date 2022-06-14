from Mob import *
from random import choice

class Ciclope(Mob):
    monedas = [6, 7, 8]
    moneda = choice(monedas)
    niveles=[8,9,10]    
    nivel = choice(niveles)
    vidaCiclope = Mob.vida * nivel
    ataqueCiclope = (Mob.ataque+1) * (nivel+2)

    def mostrar(self):
        print(f"Vida: {Ciclope.vidaCiclope} Ataque: {Ciclope.ataqueCiclope} Nivel: {Ciclope.nivel}")
    
    def expCiclope(self):
        print(f"Ha otorgado {Ciclope.nivel * 5} de exp")

    def monCiclope(self):
        print(f"Ha otorgado {(Ciclope.nivel * Ciclope.moneda) - 2} monedas de oro")
    
