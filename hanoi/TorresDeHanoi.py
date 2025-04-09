from nodo.NodoPoliHanoi import NodoHanoi

class TorresDeHanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.torres = {
            'A': [NodoHanoi(i) for i in range(num_discos, 0, -1)],
            'B': [],
            'C': []
        }

    def mover_disco(self, origen, destino):
        disco = self.torres[origen].pop()
        self.torres[destino].append(disco)
        print(f"Mover disco {disco.valor} de {origen} a {destino}")

    def resolver_hanoi(self, n, origen, auxiliar, destino):
        if n == 1:
            self.mover_disco(origen, destino)
        else:
            self.resolver_hanoi(n - 1, origen, destino, auxiliar)
            self.mover_disco(origen, destino)
            self.resolver_hanoi(n - 1, auxiliar, origen, destino)

    def jugar(self):
        print("Estado inicial:")
        self.imprimir_torres()
        self.resolver_hanoi(self.num_discos, 'A', 'B', 'C')
        print("Estado final:")
        self.imprimir_torres()

    def imprimir_torres(self):
        for torre, discos in self.torres.items():
            print(f"Torre {torre}: {[disco.valor for disco in discos]}")
        print()

class ProblemaHanoi:
    def __init__(self, n):
        self.n = n
    try:
        num_discos = int(input("Introduce el número de discos: "))
        if num_discos <= 0:
            raise ValueError("El número de discos debe ser mayor que 0.")
        juego = TorresDeHanoi(num_discos)
        juego.jugar()
    except ValueError as e:
        print(f"Error: {e}")