import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de SQLAlchemy
Base = declarative_base()
engine = create_engine('sqlite:///reinas_movimientos.db', echo=True)  # Base de datos SQLite
Session = sessionmaker(bind=engine)

# Definición del modelo para la tabla 'movimientos_reinas'
class MovimientoReinas(Base):
    __tablename__ = 'movimientos_reinas'
    
    id = Column(Integer, primary_key=True)
    n = Column(Integer, nullable=False)  # Tamaño del tablero (n)
    movimiento = Column(String, nullable=False)  # Movimiento como lista de posiciones (ej. "[(0, 0)]")

# Crear la tabla en la base de datos
Base.metadata.create_all(engine)

# Función para guardar los movimientos en la base de datos
def guardar_movimientos_en_db(n, movimientos):
    session = Session()
    
    for movimiento in movimientos:
        movimiento_db = MovimientoReinas(
            n=n,
            movimiento=str(movimiento)  # Guardar el movimiento como cadena
        )
        session.add(movimiento_db)
    
    print(f"Se guardaron {len(movimientos)} movimientos para n={n}.")
    session.commit()
    session.close()

# Función para consultar los movimientos guardados
def consultar_movimientos():
    session = Session()
    print("\nConsultando movimientos guardados en la base de datos:")
    for movimiento in session.query(MovimientoReinas).order_by(MovimientoReinas.n):
        print(f"n={movimiento.n}, Movimiento={movimiento.movimiento}")
    session.close()

# Clase principal adaptada para recibir movimientos desde reinas.py
class JuegoReinas:
    @staticmethod
    def guardar_movimientos(n, movimientos):
        if movimientos:
            print(f"\nGuardando movimientos para n={n} en la base de datos...")
            guardar_movimientos_en_db(n, movimientos)
        else:
            print("No se encontraron movimientos para guardar.")
        consultar_movimientos()  # Mostrar lo que se guardó
