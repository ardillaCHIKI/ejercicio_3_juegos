import os
import sys
import subprocess

def main():
    # Ruta al archivo principal del juego
    game_file = os.path.join(os.path.dirname(__file__), 'caballo.py')

    # Verifica si el archivo existe
    if not os.path.isfile(game_file):
        print("Error: No se encontró el archivo 'caballo.py'.")
        sys.exit(1)

    # Ejecuta el archivo principal del juego de forma segura
    try:
        subprocess.run([sys.executable, game_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar 'caballo.py': {e}")
        sys.exit(1)
