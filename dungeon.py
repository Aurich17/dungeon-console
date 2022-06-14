#Metas: Python 1 mes a full, Java 2do mes y 3er mes Conexion base de datos: MySQL y PHP 
from random import choice
from Jugador import *
from Mago import *
from Barbaro import *
from Caballero import *
from Mob import *
from Ogro import *
from Duende import *
from Ciclope import *
raza = 0
x = 0
cofre = ["Armadura", "Tunica", "Varita", "Pociones", "escudo", "Generador de Montura"]
while True:
    if x == 0:
        print("Podras tomar acciones con las siguientes letras: S para sí y N para no")
        x += 1
    juego = input("¿Quieres iniciar un nuevo Juego? ---> ").upper()
    #Verificando si el jugador quiere inciar el juego
    if juego == "S":
        if x == 1:
            print("Aventurero tu nueva historia empieza ahora, por favor dinos tu nombre:")
            nombre = input("Nombre: ")
            if len(nombre) > 3:
                print(f"Mucho gusto {nombre}, ahora podrias decirno a que raza perteneces: ")
                while raza != 1 and raza != 2 and raza != 3:
                    #Seleccion de razas
                    print(f"""
                    ---RAZAS---
                    1.Mago
                    2.Caballero
                    3.Barbaro""")
                    raza = input("¿A que raza perteneces? ---> ")
                    if raza == "1" or raza == "2" or raza == "3":
                        #Funcion que retorna la eleccion del jugador
                        def darRaza():
                            return raza
                        break
                    else:
                        print("Opción no valida, por favor vuelve a escoger")
                #Pasando el valor a la variable
                raza = darRaza()
                print(f"Este es el numero de la raza {raza}")
                razas = {"1": "Mago", "2": "Caballero", "3": "Barbaro"}
                razaJugador = razas[raza]
                print(f"La raza que seleccionaste es: {razaJugador}")
                #Creando el jugador.Ya sea Mago, Cabllero o Barbaro para
                if raza == "1":
                    newPlayer = Mago(nombre, razaJugador)
                    print(newPlayer.raza)
                    newPlayer.informacion()
                elif raza == "2":
                    newPlayer = Caballero(nombre, razaJugador)
                elif raza == "3":
                    print("Barbaro creacion")
                    newPlayer = Barbaro(nombre, razaJugador)
                juego = input(f"Quieres ver tus estadisticas? ---> ").upper()
                if juego == "S":
                    newPlayer.informacion()
                    break

            else:
                print("El nombre debe de contener mas de 3 caracteres")
    elif juego == "N":
        break
    else:
        print("Acción no admitida")
    

