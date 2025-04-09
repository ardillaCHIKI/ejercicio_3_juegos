class NodoHanoi(object):
    def __init__(self, disco, origen, destino, auxiliar):
        """
        Constructor para el nodo de las Torres de Hanoi.

        :param disco: Número del disco (1 es el más pequeño).
        :param origen: Torre de origen.
        :param destino: Torre de destino.
        :param auxiliar: Torre auxiliar.
        """
        self.disco = disco
        self.origen = origen
        self.destino = destino
        self.auxiliar = auxiliar

    def __str__(self):
        """
        Representación en cadena del nodo.
        """
        return f"Disco {self.disco}: {self.origen} -> {self.destino} (Auxiliar: {self.auxiliar})"