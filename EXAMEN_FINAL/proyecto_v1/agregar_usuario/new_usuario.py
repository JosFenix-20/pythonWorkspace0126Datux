import sqlite3
from rich.console import Console
from config.config import ConfigBd

console = Console()
config = ConfigBd()
conn = config.bd

def agregar_usuario():
    cursor = conn.cursor()
    try:
        nuevo_usuario = ('joseph@sistema.com','cod123','Joseph','De la cruz','admin',1)
                
        cursor.execute('''
                    INSERT OR REPLACE INTO usuarios_sistema 
                    (email, password, nombre, apellido, tipo_usuario, estado)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', nuevo_usuario)
        
        conn.commit()
        conn.close()

        console.print("[bold green]Usuario agregado correctamente[/bold green]")
        console.print(f"Email: {nuevo_usuario[0]}")
        console.print(f"Contraseña: {nuevo_usuario[1]}")
    
    except sqlite3.Error as e:
            print(f"❌ Error al agregar a la base de datos: {e}")
            conn.rollback()
            return False
    finally:
            config.discontecBd()

"""
joseph@sistema.com
cod123
"""