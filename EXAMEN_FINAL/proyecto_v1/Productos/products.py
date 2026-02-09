from rich.console import Console
from config.config import ConfigBd

console = Console()
config = ConfigBd()
path="C:\\Users\\FENIX\\Documents\\CODE_VISUAL\\DATUX_Temp\\EXAMEN_FINAL\\proyecto_v1\\Productos\\reporte.txt"

def mostrarGraficas():
    conn = config.bd
    cursor = conn.cursor()

    cursor.execute("""
        SELECT tipo_propiedad, COUNT(*) as cantidad
        FROM productos
        GROUP BY tipo_propiedad
    """)
    resultadosTipo_propiedad = cursor.fetchall()
    cursor.execute("""
        SELECT direccion, COUNT(*) as cantidad
        FROM productos
        GROUP BY direccion
    """)
    resultadosDireccion = cursor.fetchall()

    console.print("\n[green]>>> Por propietario: [/green]")
    guardado(resultadosTipo_propiedad,path)
    
    console.print("\n[green]>>> Por Direccion: [/green]")
    guardado(resultadosDireccion,path)

def guardado(resultados,path):
    if not resultados:
        console.print("[bold red]No hay datos[/bold red]")
        return

    max_val = max([fila[1] for fila in resultados])
    with open(path, "a", encoding="utf-8") as f:
        
        for tipo, cantidad in resultados:
            bar = "█" * int((cantidad / max_val) * 10)
            linea = f"{tipo:15} {bar} {cantidad}"
            console.print(linea)
            f.write(linea + "\n")

def limpiarTXT():
    with open(path, "w", encoding="utf-8") as f:
        pass

def leerTXT():
    with open(path, "r", encoding="utf-8") as f:
        contenido = f.read()
    return contenido
