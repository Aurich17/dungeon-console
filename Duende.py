from Mob import *
from random import choice

class Duende(Mob):
    monedas = [1,2,3]
    moneda = choice(monedas)
    niveles = [1, 2, 3]
    nivel = choice(niveles)
    vidaDuende = Mob.vida * nivel
    ataqueDuende = (Mob.ataque-2) * nivel

    def mostrar(self):
        print(f"Vida: {Duende.vidaDuende} Ataque: {Duende.ataqueDuende} Nivel: {Duende.nivel}")
    
    def expDuende(self):
        print(f"Ha otorgado {Duende.nivel * 3} de exp")

    def monDuende(self):
        print(f"Ha otorgado {(Duende.nivel * Duende.moneda)} monedas de oro")

