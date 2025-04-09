import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from nodo.NodoPolinomio import NodoPolinomio  # Importar la clase NodoPolinomio

def resolver_n_reinas_con_nodos(n):
    raiz = NodoPolinomio([[0 for _ in range(n)] for _ in range(n)], 0)
    pila = [raiz]

    while pila:
        nodo_actual = pila.pop()
        if nodo_actual.nivel == n:
            return nodo_actual.estado

        nodo_actual.generar_hijos(n)
        pila.extend(nodo_actual.hijos)

    return None


def n_reinas():
    try:
        n = int(input("Introduce el número de reinas (y el tamaño del tablero): "))
        solucion = resolver_n_reinas_con_nodos(n)
        if solucion:
            for fila in solucion:
                print(fila)
        else:
            print(0)
    except ValueError:
        print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    n_reinas()
