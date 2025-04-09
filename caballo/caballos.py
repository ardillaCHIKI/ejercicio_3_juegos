import random
from abc import ABC, abstractmethod 
from nodo.Nodo import NodoConcreto


class Caballo(NodoConcreto):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.movimientos = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

    def es_movimiento_valido(self, x, y, tablero):
        return 0 <= x < 8 and 0 <= y < 8 and tablero[x][y] == -1

    def resolver_problema_caballo(self):
        # Crear un tablero 8x8 inicializado con -1
        tablero = [[-1 for _ in range(8)] for _ in range(8)]

        # Posición inicial aleatoria
        x, y = random.randint(0, 7), random.randint(0, 7)
        tablero[x][y] = 0  # Marcar la posición inicial
        print(f"Posición inicial: ({x}, {y})")

        # Resolver el problema usando backtracking
        if self._resolver_caballo(x, y, 1, tablero):
            self.imprimir_tablero(tablero)
        else:
            print("No se encontró solución.")

    def _resolver_caballo(self, x, y, movimiento_actual, tablero):
        if movimiento_actual == 64:  # Si se han realizado los 64 movimientos
            return True

        for dx, dy in self.movimientos:
            nuevo_x, nuevo_y = x + dx, y + dy
            if self.es_movimiento_valido(nuevo_x, nuevo_y, tablero):
                tablero[nuevo_x][nuevo_y] = movimiento_actual
                print(f"Movimiento {movimiento_actual}: ({nuevo_x}, {nuevo_y})")  # Imprimir cada movimiento
                if self._resolver_caballo(nuevo_x, nuevo_y, movimiento_actual + 1, tablero):
                    return True
                # Backtracking
                tablero[nuevo_x][nuevo_y] = -1

        return False

    def imprimir_tablero(self, tablero):
        for fila in tablero:
            print(" ".join(f"{celda:2}" for celda in fila))

if __name__ == "__main__":
    caballo = Caballo(0, 0)
    caballo.resolver_problema_caballo()