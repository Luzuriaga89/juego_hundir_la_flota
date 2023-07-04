import random 
import numpy as np

import Mis_funciones

mi_tablero_disparos = np.full((10,10)," ")
print(mi_tablero_disparos)
print()

mi_tablero_barcos = np.full((10, 10), " ")

# Posicionar los barcos 
for i in range(2):
    while True:
        if Mis_funciones.posicionar_mi_barco(mi_tablero_barcos, 3):
            break

for i in range(3):
    while True:
        if Mis_funciones.posicionar_mi_barco(mi_tablero_barcos, 2):
            break

for i in range(4):
    while True:
        if Mis_funciones.posicionar_mi_barco(mi_tablero_barcos, 1):
            break
while True:
    if Mis_funciones.posicionar_mi_barco(mi_tablero_barcos, 4):
        break

print(mi_tablero_barcos)
print()
tablero_maq_disparos= np.full((10,10)," ")
print(tablero_maq_disparos)
print()

Mis_funciones.posicionar_barco

tablero_maq_barcos = np.full((10, 10), " ")

# Posicionar los barcos 
for i in range(2):
    while True:
        if Mis_funciones.posicionar_barco(tablero_maq_barcos, 3):
            break

for i in range(3):
    while True:
        if Mis_funciones.posicionar_barco(tablero_maq_barcos, 2):
            break

for i in range(4):
    while True:
        if Mis_funciones.posicionar_barco(tablero_maq_barcos, 1):
            break
while True:
    if Mis_funciones.posicionar_barco(tablero_maq_barcos, 4):
        break

print(tablero_maq_barcos)

x = 1
while x < 5:
    while True: #mi turno
        print("Turno del jugador")
        
        fila, columna = Mis_funciones.disparos()
            
        if tablero_maq_barcos[fila][columna] == "B":
            print("Barco")

            tablero_maq_barcos[fila, columna] = "X"
            mi_tablero_disparos[fila, columna] = "X"

            print(mi_tablero_disparos)

        elif tablero_maq_barcos[fila][columna] == "X" or tablero_maq_barcos[fila][columna] == "A":
            print("Ya has disparado antes en esas coordenadas, vuelve a disparar")

        elif tablero_maq_barcos[fila][columna] == " ":
            print("Agua")

            tablero_maq_barcos[fila, columna] = "A"
            mi_tablero_disparos[fila, columna] = "A"

            print(mi_tablero_disparos)
            break

        else:
            break

    if (tablero_maq_barcos != "B").all():
        print("Ha ganado el jugador")
        break

    while True: #turno maquina

        print("Turno de la máquina")

        fila = np.random.randint(0, 9)
        columna = np.random.randint(0,9)
    
        if mi_tablero_barcos[fila][columna] == "B":
            print("Barco")

            mi_tablero_barcos[fila, columna] = "X"
            tablero_maq_disparos[fila, columna] = "X"

            print(tablero_maq_disparos)

        elif mi_tablero_barcos[fila][columna] == "X" or mi_tablero_barcos[fila][columna] == "A":
            print("Ya has disparado antes en esas coordenadas, vuelve a disparar")

        elif mi_tablero_barcos[fila][columna] == " ":
            print("Agua")

            mi_tablero_barcos[fila, columna] = "A"
            tablero_maq_disparos[fila, columna] = "A"

            print(tablero_maq_disparos)
            break

        else:
            break
    
    if (mi_tablero_barcos != "B").all():
        print("Ha ganado la máquina")
        break

x += 1

print(mi_tablero_disparos)
print()
print(mi_tablero_barcos)