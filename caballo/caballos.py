import sys
import os
import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from abc import ABC, abstractmethod 
from nodo.Nodo import Nodo

class TableroCaballo:
    def __init__(self, n):
        self.n = n  # Tamaño del tablero (n x n)
        self.tablero = [[-1 for _ in range(n)] for _ in range(n)]  # -1 significa no visitado
        # Posibles movimientos del caballo (8 movimientos en L)
        self.movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
        self.movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]
        self.solucion_encontrada = False
        self.recorrido = []  # Lista para guardar el recorrido

    def es_valido(self, x, y):
        # Verifica si la posición está dentro del tablero y no ha sido visitada
        return (0 <= x < self.n and 0 <= y < self.n and 
                self.tablero[x][y] == -1)

    def resolver(self, x_inicial, y_inicial):
        # Coloca el primer movimiento
        self.tablero[x_inicial][y_inicial] = 0
        self.recorrido.append(Nodo.create_with_movement(x_inicial, y_inicial, 0))
        
        # Intenta resolver desde la posición inicial
        if self.resolver_util(x_inicial, y_inicial, 1):
            self.solucion_encontrada = True
            return True
        return False

    def resolver_util(self, x, y, movimiento_actual):
        # Si hemos visitado todas las casillas, terminamos
        if movimiento_actual == self.n * self.n:
            return True

        # Prueba todos los posibles movimientos
        for i in range(8):
                nuevo_x = x + self.movimientos_x[i]
                nuevo_y = y + self.movimientos_y[i]
                
                if self.es_valido(nuevo_x, nuevo_y):
                    self.tablero[nuevo_x][nuevo_y] = movimiento_actual
                    nuevo_nodo = Nodo.create_with_movement(nuevo_x, nuevo_y, movimiento_actual)
                    self.recorrido.append(nuevo_nodo)
                    
                    if self.resolver_util(nuevo_x, nuevo_y, movimiento_actual + 1):
                        return True
                    
                    # Backtracking: si no funciona, deshacemos el movimiento
                    self.tablero[nuevo_x][nuevo_y] = -1
                    self.recorrido.pop()
            
        return False

    def imprimir_tablero(self):
        print("\nTablero con movimientos:")
        for fila in self.tablero:
            print(" ".join(f"{num:2d}" for num in fila))

    def imprimir_recorrido(self):
        print("\nRecorrido del caballo:")
        for nodo in self.recorrido:
            print(f"Movimiento {nodo.movimiento}: ({nodo.x}, {nodo.y})")

    def imprimir_vectores(self):
        print("\nVectores de posición del caballo:")
        for i in range(1, len(self.recorrido)):
            x1, y1 = self.recorrido[i - 1].x, self.recorrido[i - 1].y
            x2, y2 = self.recorrido[i].x, self.recorrido[i].y
            vector = (x2 - x1, y2 - y1)
            print(f"Vector {i}: {vector}")

# Función principal para probar el código
def ProblemaCaballo():
    tamaño = 8  # Tablero 8x8
    caballo = TableroCaballo(tamaño)
    
    # Posición inicial aleatoria
    x_inicial = random.randint(0, tamaño - 1)
    y_inicial = random.randint(0, tamaño - 1)
    
    print(f"Intentando resolver el problema del caballo desde ({x_inicial}, {y_inicial})")
    
    if caballo.resolver(x_inicial, y_inicial):
        caballo.imprimir_tablero()
        caballo.imprimir_recorrido()
        caballo.imprimir_vectores()
    else:
        print("No se encontró solución desde la posición inicial")



if __name__ == "__main__":
    ProblemaCaballo()