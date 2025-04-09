class NodoPolinomio(object):
    def __init__(self, estado, nivel):
        self.estado = estado
        self.nivel = nivel

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