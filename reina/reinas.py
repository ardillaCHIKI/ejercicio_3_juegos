import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from nodo.NodoPolinomio import NodoPolinomio  # Importar la clase NodoPolinomio

def resolver_n_reinas_con_nodos(n):
    raiz = NodoPolinomio([[0 for _ in range(n)] for _ in range(n)], 0)
    pila = [raiz]

    def es_valido(estado, fila, col):
        for i in range(fila):
            if estado[i][col] == 1 or \
                (col - (fila - i) >= 0 and estado[i][col - (fila - i)] == 1) or \
                (col + (fila - i) < len(estado) and estado[i][col + (fila - i)] == 1):
                return False
        return True

    while pila:
        nodo_actual = pila.pop()
        if nodo_actual.nivel == n:
            return nodo_actual.estado

        for col in range(n):
            if es_valido(nodo_actual.estado, nodo_actual.nivel, col):
                nuevo_estado = [fila[:] for fila in nodo_actual.estado]
                nuevo_estado[nodo_actual.nivel][col] = 1
                pila.append(NodoPolinomio(nuevo_estado, nodo_actual.nivel + 1))

    return None  # Si no se encuentra solución, devolver None

def imprimir_solucion(estado):
    print("Solución encontrada:")
    posiciones = []
    for i, fila in enumerate(estado):
        for j, valor in enumerate(fila):
            if valor == 1:
                posiciones.append((i, j))
        print(" ".join("Q" if x == 1 else "." for x in fila))
    print(f"Posiciones de las reinas: {posiciones}")
    return posiciones

class JuegoReinas:
    try:
        n = int(input("Introduce el número de reinas (y tamaño del tablero): "))
        if n <= 0:
            print("El número de reinas debe ser mayor que 0.")
        else:
            solucion = resolver_n_reinas_con_nodos(n)
            if solucion:
                posiciones = imprimir_solucion(solucion)
                print(f"Las posiciones de las reinas son: {posiciones}")
            else:
                print("No se encontró solución.")
    except ValueError:
        print("Por favor, introduce un número entero válido.")
