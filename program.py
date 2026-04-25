import random

class Equipo:
    def _init_(self, nombre="", partidosganados=0, partidosperdidos=0, setganados=0):
        self.nombre = nombre
        self.partidosganados = partidosganados
        self.partidosperdidos = partidosperdidos
        self.setganados = setganados

    def _str_(self):
        return f"Equipo: {self.nombre}"


equipo1 = Equipo()
equipo2 = Equipo()


def Puntos():
    return random.randint(10, 28)

def Puntosextras():
    return random.randint(0, 6)

def RegistrarSet(nroequipo):
    if nroequipo == 1:
        ganador, rival = equipo1, equipo2
    else:
        ganador, rival = equipo2, equipo1
    ganador.setganados += 1
    
    print(f"\n> Set para: {ganador.nombre}")
    print(f"  Marcador Actual: {equipo1.nombre} ({equipo1.setganados}) - {equipo2.nombre} ({equipo2.setganados})")
    
    if ganador.setganados == 3:
        ganador.partidosganados += 1
        rival.partidosperdidos += 1
        print(f"\n¡Gano el equipo :{ganador.nombre}")     
        equipo1.setganados = 0
        equipo2.setganados = 0
        return True
    return False

def JugarPartido():
    print(f"\n--- Iniciando partido: Equipo 1: {equipo1.nombre} Equipo 2: {equipo2.nombre} ---")
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
    print("\n--- RESUMEN DEL TORNEO ---")
    print(f" {equipo1.nombre} G: {equipo1.partidosganados} | P: {equipo1.partidosperdidos}")
    print(f" {equipo2.nombre} G: {equipo2.partidosganados} | P: {equipo2.partidosperdidos}")
   

# 3. Menú Principal
while True:
    print("\n--- SISTEMA DE GESTIÓN DE VOLEY ---")
    print("1. Iniciar Torneo (Registrar y Jugar)")
    print("2. Salir")
    
    try:
        opc = int(input("Seleccione una opción: "))
        
        if opc == 1:
            equipo1.nombre = input("\nNombre del Equipo 1: ")
            equipo2.nombre = input("Nombre del Equipo 2: ")
            n_partidos = int(input(f"¿Cuántos partidos jugarán {equipo1.nombre} contra {equipo2.nombre}?: "))
            
            for i in range(n_partidos):
                print(f"\n--- ENFRENTAMIENTO #{i+1} ---")
                JugarPartido()
            
            # Al terminar todos los partidos, mostrar tabla final
            ResultadoTorneo()
            
        elif opc == 2:
            print("Cerrando el sistema")
            break
        else:
            print("Opción no válida, intente de nuevo.")
            
    except ValueError:
        print("Error: Por favor ingrese solo números.")
