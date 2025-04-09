class Nodo:
    def __init__(self, x, y, tipo=None):
        self.x = x
        self.y = y
        self.tipo = tipo  # Tipo puede ser 'caballo', 'reina', etc.

    @staticmethod
    def create_with_movement(x, y, movimiento, tipo=None):
        nodo = Nodo(x, y, tipo)
        nodo.movimiento = movimiento
        return nodo

    def __str__(self):
        return f"Nodo({self.x}, {self.y}, tipo={self.tipo})"