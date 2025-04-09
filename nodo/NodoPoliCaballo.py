class NodoCaballo:
    def __init__(self, posicion):
        """
        Inicializa un nodo para el caballo en el ajedrez.
        
        :param posicion: Una tupla (x, y) que representa la posición del caballo en el tablero.
        """
        self.posicion = posicion

    def movimientos_posibles(self):
        """
        Calcula los movimientos posibles del caballo desde su posición actual.
        
        :return: Una lista de tuplas con las posiciones posibles.
        """
        x, y = self.posicion
        movimientos = [
            (x + 2, y + 1), (x + 2, y - 1),
            (x - 2, y + 1), (x - 2, y - 1),
            (x + 1, y + 2), (x + 1, y - 2),
            (x - 1, y + 2), (x - 1, y - 2)
        ]
        # Filtrar movimientos que estén dentro del tablero (8x8)
        return [(nx, ny) for nx, ny in movimientos if 0 <= nx < 8 and 0 <= ny < 8]