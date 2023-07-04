import random 
import numpy as np 

def posicionar_mi_barco(tablero, longitud):
    # Generar una posición aleatoria para el barco
    fila = np.random.randint(0, 10)
    columna = np.random.randint(0, 11 - longitud)

    #verificar posicion
    if np.all(tablero[fila, columna:columna+longitud] == " "):

        tablero[fila, columna:columna+longitud] = "B"
        return True
    
    return False


def posicionar_barco(tablero, longitud):
    # Generar una posición aleatoria para el barco
    fila = np.random.randint(0, 10)
    columna = np.random.randint(0, 11 - longitud) 

    #verificar posicion
    if np.all(tablero[fila, columna:columna+longitud] == " "):

        tablero[fila, columna:columna+longitud] = "B"
        return True

    return False


def disparos():
    while True:
        try:
            fila = int(input("Introduce la fila del 0 al 9: "))
            columna = int(input("Introduce la columna del 0 al 9: "))
            if fila < 0 or fila > 9 or columna < 0  or columna > 9:
                print("Introducir valores correctos")
            else:
                return fila, columna
        except ValueError:
            print("Valores incorrectos, vuelve a introducir valores")

