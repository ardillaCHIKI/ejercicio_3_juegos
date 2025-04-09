import random
from nodo.NodoPoliCaballo import NodoCaballo

class TableroCaballo:
    def __init__(self, n):
        self.n = n  # Tamaño del tablero (n x n)
        self.tablero = [[-1 for _ in range(n)] for _ in range(n)]  # -1 significa no visitado
        self.movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
        self.movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]
        self.recorrido = []
        self.solucion_encontrada = False

    def es_valido(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and self.tablero[x][y] == -1

    def resolver(self):
        x_inicial = random.randint(0, self.n - 1)
        y_inicial = random.randint(0, self.n - 1)
        print(f"Posición inicial aleatoria: ({x_inicial}, {y_inicial})")

        self.tablero[x_inicial][y_inicial] = 0
        self.recorrido.append(NodoCaballo.create_with_movement(x_inicial, y_inicial, 0))

        if self.resolver_util(x_inicial, y_inicial, 1):
            self.solucion_encontrada = True
            return True
        return False

    def resolver_util(self, x, y, movimiento_actual):
        if movimiento_actual == self.n * self.n:
            return True

        for i in range(8):
            nuevo_x = x + self.movimientos_x[i]
            nuevo_y = y + self.movimientos_y[i]

            if self.es_valido(nuevo_x, nuevo_y):
                print(f"Movimiento {movimiento_actual}: ({x}, {y}) -> ({nuevo_x}, {nuevo_y})")
                self.tablero[nuevo_x][nuevo_y] = movimiento_actual
                nuevo_nodo = NodoCaballo.create_with_movement(nuevo_x, nuevo_y, movimiento_actual)
                self.recorrido.append(nuevo_nodo)

                if self.resolver_util(nuevo_x, nuevo_y, movimiento_actual + 1):
                    return True

                self.tablero[nuevo_x][nuevo_y] = -1
                self.recorrido.pop()

        return False

    def resolver_util(self, x, y, movimiento_actual):
        if movimiento_actual == self.n * self.n:
            return True

        for i in range(8):
            nuevo_x = x + self.movimientos_x[i]
            nuevo_y = y + self.movimientos_y[i]

            if self.es_valido(nuevo_x, nuevo_y):
                self.tablero[nuevo_x][nuevo_y] = movimiento_actual
                nuevo_nodo = NodoCaballo.create_with_movement(nuevo_x, nuevo_y, movimiento_actual)
                self.recorrido.append(nuevo_nodo)

                if self.resolver_util(nuevo_x, nuevo_y, movimiento_actual + 1):
                    return True

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

    def imprimir_posiciones(self):
        print("\nPosiciones del caballo durante la solución:")
        for nodo in self.recorrido:
            print(f"({nodo.x}, {nodo.y})")


class ProblemaCaballo:
    tamaño = 8
    caballo = TableroCaballo(tamaño)

    print("Intentando resolver el problema del caballo con posición inicial aleatoria")

    if caballo.resolver():
        print(caballo.imprimir_tablero())
        print(caballo.imprimir_recorrido())
        print(caballo.imprimir_vectores())
        print(caballo.imprimir_posiciones())
    else:
        print("No se encontró solución desde la posición inicial aleatoria")

