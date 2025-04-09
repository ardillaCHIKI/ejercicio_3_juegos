# ejercicio_3_juegos
https://github.com/ardillaCHIKI/ejercicio_3_juegos.git
## Problema del Caballo

El problema del caballo es un desafío clásico de ajedrez que consiste en encontrar un recorrido cerrado o abierto en el que el caballo visite cada casilla del tablero exactamente una vez.

### Fórmula Matemática

El problema puede resolverse utilizando un enfoque de backtracking o algoritmos como Warnsdorff. Matemáticamente, se puede representar como un grafo donde:

- Cada casilla del tablero es un nodo.
- Cada movimiento válido del caballo es una arista.

El objetivo es encontrar un **camino hamiltoniano** (recorrido abierto) o un **ciclo hamiltoniano** (recorrido cerrado) en este grafo.

### Representación del Movimiento del Caballo

El movimiento del caballo en un tablero de ajedrez se define por las siguientes coordenadas relativas:

```
(x ± 2, y ± 1) 
(x ± 1, y ± 2)
```

Donde `(x, y)` es la posición actual del caballo.

### Algoritmo de Backtracking

1. Coloca el caballo en una casilla inicial.
2. Intenta mover el caballo a una casilla no visitada siguiendo las reglas del ajedrez.
3. Si no hay movimientos válidos y no se han visitado todas las casillas, retrocede al paso anterior.
4. Repite hasta encontrar una solución o determinar que no existe.

```