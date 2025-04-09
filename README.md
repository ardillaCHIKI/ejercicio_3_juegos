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

### JUEGO DE LAS N-REINAS
Este proyecto implementa una solución al problema clásico de las n-reinas utilizando una estructura de nodos y un enfoque basado en pila (stack). El objetivo es colocar n reinas en un tablero de ajedrez de tamaño n x n de manera que ninguna reina se amenace entre sí (es decir, no compartan fila, columna ni diagonal).

El programa está escrito en Python y permite al usuario ingresar el tamaño del tablero (n) a través de la terminal, mostrando una solución en formato textual si existe.

Características
Resuelve el problema de las n-reinas para un tablero de tamaño n x n.
Usa una representación matricial del tablero (n x n) donde 1 indica la posición de una reina y 0 indica una casilla vacía.
Muestra la solución en la consola con "Q" para reinas y "." para casillas vacías, junto con las posiciones (fila, columna) de las reinas.
Maneja errores de entrada (valores no numéricos o negativos).

### TORRES DE HANOI
Este proyecto implementa una solución al problema clásico de las Torres de Hanoi en Python. El problema consiste en mover una pila de discos de diferentes tamaños desde una torre de origen (A) a una torre de destino (C), utilizando una torre auxiliar (B), siguiendo estas reglas:

Solo se puede mover un disco a la vez.
Un disco más grande no puede colocarse sobre uno más pequeño.
Solo se puede mover el disco superior de una torre.
El programa utiliza una representación basada en objetos y nodos (NodoHanoi) para simular las torres y muestra los pasos de la solución en la terminal.

Características
Resuelve el problema de las Torres de Hanoi para un número dado de discos (n).
Usa una estructura de tres torres (A, B, C) representadas como listas de nodos.
Muestra cada movimiento de disco y los estados inicial y final de las torres.
Incluye manejo de errores para entradas inválidas.
