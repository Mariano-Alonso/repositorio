import random

class Equipo:
    def __init__(self, nombre="", partidosganados=0, partidosperdidos=0, setganados=0):
        self.nombre = nombre
        self.partidosganados = partidosganados
        self.partidosperdidos = partidosperdidos
        self.setganados = setganados

    def __str__(self):
        return f"Equipo: {self.nombre}"


e1 = Equipo()
e2 = Equipo()


def Puntos():
    return random.randint(10, 28)

def Puntosextras():
    return random.randint(0, 6)

def RegistrarSet(nroequipo):
    if nroequipo == 1:
        ganador, r = e1, e2
    else:
        ganador, rl = e2, e1

    ganador.setganados += 1
    
    print(f"\n> Set para: {ganador.nombre}")
    print(f"Marcador Actual: {e1.nombre} ({e1.setganados}) - {e2.nombre} ({e2.setganados})")
    
    if ganador.setganados == 3:
        ganador.partidosganados += 1
        r.partidosperdidos += 1
        print(f"\n¡Ganó el equipo: {ganador.nombre}!")     
        e1.setganados = 0
        e2.setganados = 0
        return True

    return False


def JugarPartido():
    print(f"\n--- Partido: {e1.nombre} vs {e2.nombre} ---")
    termino = False

    while not termino:
        p1 = Puntos()
        p2 = Puntos()

        while p1 < 25 and p2 < 25:
            p1 += Puntosextras()
            p2 += Puntosextras()
        
        if p1 > p2:
            termino = RegistrarSet(1)
        else:
            termino = RegistrarSet(2)


def ResultadoTorneo():
    print("\n--- RESULTADO FINAL ---")
    print(f"{e1.nombre} → Ganados: {e1.partidosganados} | Perdidos: {e1.partidosperdidos}")
    print(f"{e2.nombre} → Ganados: {e2.partidosganados} | Perdidos: {e2.partidosperdidos}")


while True:
    print("\n SISTEMA DE VOLEY")
    print("1. Iniciar")
    print("2. Salir")
    
    try:
        opc = int(input("eliga una opción: "))
        
        if opc == 1:
            e1.nombre = input("\nNombre del Equipo 1: ")
            e2.nombre = input("Nombre del Equipo 2: ")

            n_partidos = int(input("¿Cuántos partidos?: "))
            
            for i in range(n_partidos):
                print(f"\n--- PARTIDO #{i+1} ---")
                JugarPartido()

            ResultadoTorneo() 

        elif opc == 2:
            print("")
            break
        else:
            print("Error")
            
    except ValueError:
        print("solo numeros")
