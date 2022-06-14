from Mob import *
from random import choice

class Ogro(Mob):
    monedas = [4,5]
    moneda = choice(monedas)
    niveles = [4, 5, 6, 7]
    nivel = choice(niveles)
    vidaOgro = Mob.vida * nivel 
    ataqueOgro = (Mob.ataque-1) * nivel

    def mostrar(self):
        print(f"Vida: {Ogro.vidaOgro} - Ataque: {Ogro.ataqueOgro} - Nivel: {Ogro.nivel}")
    
    def expOgro(self):
        print(f"Ha otorgado {Ogro.nivel * 4} de exp")

    def monOgro(self):
        print(f"Ha otorgado {(Ogro.nivel * Ogro.moneda) - 2} monedas de oro")


