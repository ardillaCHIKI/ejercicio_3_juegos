class NodoHanoi(object):
    def __init__(self, disco, origen=None, destino=None, auxiliar=None):
        self.disco = disco
        self.origen = origen
        self.destino = destino
        self.auxiliar = auxiliar

    def __str__(self):
        return f"Disco {self.disco}: {self.origen} -> {self.destino} (Auxiliar: {self.auxiliar})"