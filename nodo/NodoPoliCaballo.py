class NodoCaballo:
    def __init__(self, x, y, movimiento):
        self.x = x
        self.y = y
        self.movimiento = movimiento

    @staticmethod
    def create_with_movement(x, y, movimiento):
        return NodoCaballo(x, y, movimiento)

    def movimientos_posibles(self):
        x, y = self.posicion
        movimientos = [
            (x + 2, y + 1), (x + 2, y - 1),
            (x - 2, y + 1), (x - 2, y - 1),
            (x + 1, y + 2), (x + 1, y - 2),
            (x - 1, y + 2), (x - 1, y - 2)
        ]
        # Filtrar movimientos que estén dentro del tablero (8x8)
        return [(nx, ny) for nx, ny in movimientos if 0 <= nx < 8 and 0 <= ny < 8]