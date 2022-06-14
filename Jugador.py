class Jugador():
    inventario = {}
    armadura = 0
    vida = 0
    daño = 0
    energia = 0
    montura = ""
    arma = ""
    exp = 0
    moneda = 10

    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def tomarPociones(self):
        print(f"{self.nombre} a tomado una poción, tu vida se regenera ")

    def huir(self):
        print(f"{self.nombre} a huido de la batalla")
    
    def informacion(self):
        print(f"""
        -----INFORMACION||{(self.raza).upper()}-----
        *Inventario = {Jugador.inventario}
        *Armadura   = {Jugador.armadura}
        *Vida       = {Jugador.vida}
        *Daño       = {Jugador.daño}
        *Energia    = {Jugador.energia}
        *Montura    = {Jugador.montura}
        *Arma       = {Jugador.arma}
        *EXP        = {Jugador.exp}
        *Nombre     = {self.nombre}
        ---------------------
        Saldo: {Jugador.moneda} monedas de oro""")
    
    def subirNivel(self):
        print(f"{self.nombre} a subido de nivel")
    
    def morir(self):
        print("Tu vida a llegado a cero, no puedes continuar...FIN DEL JUEGO")


#newJugador = Jugador("Frank")

#newJugador.morir()
#newJugador.huir()
#newJugador.subirNivel()
#newJugador.tomarPociones()
#newJugador.informacion()