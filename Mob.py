from random import choice
class Mob():
    ataques = [3, 4, 5, 7]
    vidas = [5, 6, 7, 8, 9, 10]
    ataque = choice(ataques) 
    vida = choice(vidas)

    def dejarHuir(self):
        x = [True, False, True, False, True]
        y = choice(x)
        print(y)



