import numpy as np
import random

tablero = np.full((10, 10), " ")

def colocar_barcos(tablero, lista_barcos):
    for barco in lista_barcos:
        for pos in barco:
            x, y = pos
            tablero[x, y] = 'O'
    return tablero

barco_1 = [(0,1)]
barco_1_2 = [(0,3)]
barco_1_3 = [(0,5)]
barco_1_4 = [(0,7)]
barco_2 = [(3,1),(3,2)]
barco_2_2 = [(3,5),(3,6)]
barco_2_3 = [(3,8), (3,9)]
barco_3 = [(5,1),(5,2),(5,3)]
barco_3_2 = [(5,7), (5,8), (5,9)]
barco_4 = [(9,1), (9,2), (9,3), (9,4)]

lista_barcos = [barco_1, barco_1_2, barco_1_3,
                barco_1_4, barco_2, barco_2_2, 
                barco_2_3, barco_3, barco_3_2, 
                barco_4]

tablero_con_barcos = colocar_barcos(tablero, lista_barcos)

# función para disparar al tablero
def disparar(tablero, x, y):
    if tablero[x, y] == 'O':
        tablero[x, y] = 'X'
        print("¡Le has dado a un barco!")
        print(tablero) 
        return True
    elif tablero[x, y] == 'X':
        print("Ya habías disparado ahí antes.")
        print(tablero) 
        return False
    else:
        tablero[x, y] = '-'
        print("Agua.")
        print(tablero) 
        return False
    
# función para que la máquina dispare al tablero
def disparar_maquina(tablero):
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if tablero[x, y] == 'O':
            tablero[x, y] = 'X'
            print("La máquina te ha dado.")
            print(tablero)
            return True
        elif tablero[x, y] == '-':
            print("La máquina ha disparado en una posición que ya había disparado antes.")
            print(tablero) 
        else:
            tablero[x, y] = '-'
            print("La máquina ha disparado en agua.")
            print(tablero) 
            return False
        
# función para verificar si se han hundido todos los barcos
def todos_barcos_hundidos(tablero):
    for i in range(10):
        for j in range(10):
            if tablero[i][j] == 'O':
                return False
    return True

# juego de hundir la flota
turno_jugador = True
while True:
    if turno_jugador:
        x = int(input("Ingresa una fila: "))
        y = int(input("Ingresa una columna: "))
        if disparar(tablero_con_barcos, x, y):
            print("¡Has hundido un barco!")
            if todos_barcos_hundidos(tablero_con_barcos):
                print("¡Felicidades, has ganado!")
                break  # Termina el juego
            turno_jugador = True  # Has acertado, otro turno
        else:
            turno_jugador = False  # Has fallado, otro turno
    else:
        if disparar_maquina(tablero):
            print("La máquina ha hundido uno de tus barcos.")
            if todos_barcos_hundidos(tablero_con_barcos):
                print("¡Has perdido!")
                break  # Termina el juego
        turno_jugador = True  # Turno del jugador