from Nodo import Nodo
class NodoPolinomio(Nodo):
    def __init__(self, estado=None, nivel=0):
        """
        Nodo específico para el problema de las N-Reinas.
        :param estado: Tablero actual del problema.
        :param nivel: Fila actual que se está procesando.
        """
        super().__init__(estado, nivel)
        self._siguiente = None  # Para mantener compatibilidad con la estructura de NodoPolinomio

    def obtener_siguiente(self):
        return self._siguiente

    def establecer_siguiente(self, nodo):
        self._siguiente = nodo

    def generar_hijos(self, n):
        """
        Genera los hijos del nodo actual colocando una reina en cada columna válida de la fila actual.
        :param n: Tamaño del tablero (n x n).
        """
        for col in range(n):
            if self.es_valido(col):
                nuevo_estado = [fila[:] for fila in self.estado]
                nuevo_estado[self.nivel][col] = 1
                hijo = NodoPolinomio(nuevo_estado, self.nivel + 1)
                self.hijos.append(hijo)

    def es_valido(self, col):
        """
        Verifica si es válido colocar una reina en la columna especificada de la fila actual.
        :param col: Columna donde se quiere colocar la reina.
        :return: True si es válido, False en caso contrario.
        """
        for i in range(self.nivel):
            if self.estado[i][col] == 1 or \
               (col - (self.nivel - i) >= 0 and self.estado[i][col - (self.nivel - i)] == 1) or \
               (col + (self.nivel - i) < len(self.estado) and self.estado[i][col + (self.nivel - i)] == 1):
                return False
        return True