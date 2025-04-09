import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar funciones desde reinas.py
from reinas import resolver_n_reinas_con_nodos, imprimir_solucion
import gradio as gr

# Función para formatear la solución para Gradio
def formatear_solucion(estado):
    if estado is None:
        return "No se encontró solución."
    
    resultado = "Solución encontrada:\n"
    posiciones = []
    for i, fila in enumerate(estado):
        for j, valor in enumerate(fila):
            if valor == 1:
                posiciones.append((i, j))
        resultado += " ".join("Q" if x == 1 else "." for x in fila) + "\n"
    resultado += f"Posiciones de las reinas: {posiciones}"
    return resultado

# Función principal para Gradio
def resolver_reinas(n):
    try:
        n = int(n)  # Convertir la entrada a entero
        if n <= 0:
            return "El número de reinas debe ser mayor que 0."
        solucion = resolver_n_reinas_con_nodos(n)
        return formatear_solucion(solucion)
    except ValueError:
        return "Por favor, introduce un número entero válido."

# Crear la interfaz de Gradio
interfaz = gr.Interface(
    fn=resolver_reinas,  # Función que procesa la entrada
    inputs=gr.Textbox(label="Introduce el número de reinas (y tamaño del tablero)"),  # Campo de entrada
    outputs=gr.Textbox(label="Solución"),  # Campo de salida
    title="Juego de las N-Reinas con Gradio",
    description="Ingresa un número entero para resolver el problema de las n-reinas y ver la solución en un tablero."
)
