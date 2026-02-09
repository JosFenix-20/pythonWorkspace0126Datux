# Realiza un menu interactivo para el sistema inmobiliario usando Rich
# libreria rich y pyfiglet
# Agregar usuarios
# realiza un login
# Cerrar session
# Crear producto 
# Listar Productos
# Detalle de un producto
# Editar producto
# Cambiar de estado 
# Registrar cliente
# evaluacion de clientes
# Listar Clientes
# Estados de cliente
# Crear transaccion de venta
# generar simulacion : Monto , TEA , Plazo
# cuota : Mxi/1-(1+i)-n
# Asociar cliente a producto
# Marcar producto como reservado o vendido
# buscador de producto
# filtro de producto
# Pagos de cliente
# documentos asociados a propiedad
# Reporte de ventas
# Reporte de ingresos 

# Analisis 
# Clases :Usuarios , Clientes
#  Fx : metodos de las clases
# caracteristicas o atributos : atributos
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.text import Text
from rich import box
import pyfiglet
from config.config import ConfigBd
import random
from usuarios.userservices import Login,WelcomeUser
from sqlite3 import Connection
from config.email import EmailService
"""producctos"""
from Productos.products import mostrarGraficas,limpiarTXT,leerTXT
from agregar_usuario.new_usuario import agregar_usuario

console = Console()
config = ConfigBd()
conn = config.bd
emailService = EmailService()

def getMenu(conn:Connection):
    """Menú principal con login y salir"""
    titulo_figlet = pyfiglet.figlet_format("SISTEMA INMOBILIARIO DATUX", font="slant")
    console.print(titulo_figlet, style="bold cyan")
    console.print() # imprime
        
    while True:
        console.clear()
        
        # Panel de bienvenida con pyfiglet

        # Opciones del menú (sin tabla)
        console.print("[bold cyan]═══════════════════════════════════════[/bold cyan]")
        console.print("[bold white]  1.[/bold white] [green]Login[/green]")
        console.print("[bold white]  2.[/bold white] [yellow]agregar usuario por defecto[/yellow]")
        console.print("[bold white]  3.[/bold white] [red]Salir[/red]")
        console.print("[bold cyan]═══════════════════════════════════════[/bold cyan]")
        console.print()
        
        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3"], default="1")
        if opcion == "1":
            # Proceso de login
            console.print("\n[bold yellow]Ingreso al Sistema[/bold yellow]")
            
            usuario = Prompt.ask("Usuario (email)")
            password = Prompt.ask("Contraseña")
            # password=True
            if usuario:
                login=Login(usuario,password,conn)
                if not login:
                    console.print(f"\n[bold red]Login incorrecto! {usuario}[/bold red]")
                    continue
                
                console.print(f"\n[bold green]Login exitoso! Bienvenido {usuario}[/bold green]")
                type_user = login['type_user']
                print(type_user)
                # Determinar qué menú mostrar según el tipo de usuario
                #tipo_usuario = ['admin',"ventas"]
                #random_element = random.choice(tipo_usuario)   
                # WelcomeUser(login['user'],emailService)
                if type_user == "admin":
                    getMenuAdmin(login)
                elif type_user == "ventas":
                    getMenuSale()
                    
            else:
                console.print("\n[bold red]Usuario o contraseña incorrectos[/bold red]")
                console.input("\nPresione Enter para continuar...")          
        #==========================================================
        # """AGREGAR USUARIO"""(EJERCICIO 1)
        #==========================================================
        elif opcion == "2":
            agregar_usuario()
            console.input("\nPresione Enter para continuar...")               
            pass
        
        elif opcion == "3":
            if Confirm.ask("\n¿Está seguro que desea salir?"):
                console.print("\n[bold green]¡Hasta luego![/bold green]")
                break
def getMenuAdmin(login):
    """Menú para administradores"""
    while True:
        console.clear()
        admin_panel = Panel(
            Text("MENÚ ADMINISTRADOR", style="bold green"),
            style="bright_green",
            box=box.DOUBLE
        )
        console.print(admin_panel)
        
        table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
        table.add_column("Opción", style="cyan", justify="center")
        table.add_column("Descripción", style="white")
        
        table.add_row("1", "Gestión de Usuarios")
        table.add_row("2", "Gestión de Propiedades")
        table.add_row("3", "Reportes Financieros")
        table.add_row("4", "Dashboard")
        table.add_row("5", "<< Historial de ventas >>")
        table.add_row("0", "Cerrar Sesión")
        
        console.print(table)
        
        opcion = Prompt.ask("Seleccione una opción", choices=["0", "1", "2", "3", "4", "5"])
        
        if opcion == "0":
            console.print("\n[yellow]Cerrando sesión...[/yellow]")
            break
#======================================================================================================
# """NUEVA FUNCION AGREGADA [Reporte de ventas segun:Tipo de propiedad, Direccion]"""(EJERCICIO 2)
#======================================================================================================
        elif opcion == "5":
            console.print("\n[blue]<< HISTORIAL DE VENTAS >>[/blue]")
            mostrarGraficas()
            #==========================================================
            # """MENSAJE"""(EJERCICIO 3)
            #==========================================================
            try:
                contenido=leerTXT()
                resultado = emailService.send_email(
                    to_email="cliente@example.com",
                    subject="Envio del Reporte de Productos(EJERCICO 3) - De la cruz Joseph",
                    message=contenido
                    )

                if resultado:
                    console.print("[green]Correo enviado exitosamente[/green]")
                else:
                    console.print("[red]Error al enviar correo[/red]")
            except Exception as e:
                console.print(f"[bold red]Error: {e}[/bold red]")
            finally:
                limpiarTXT()
            console.input("mensaje enviado temporalmente")
            console.input("Presione Enter para continuar...")
            pass

        else:
            console.input("Presione Enter para continuar...")
            pass
    conn.close()

def getMenuSale():
    """Menú para personal de ventas"""
    while True:
        console.clear()
        
        sales_panel = Panel(
            Text("MENÚ VENTAS", style="bold blue"),
            style="bright_blue",
            box=box.DOUBLE
        )
        console.print(sales_panel)
        
        table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
        table.add_column("Opción", style="cyan", justify="center")
        table.add_column("Descripción", style="white")
        
        table.add_row("1", "Ver Propiedades")
        table.add_row("2", "Registrar Cliente")
        table.add_row("3", "Nueva Venta")
        table.add_row("4", "Mis Ventas")
        table.add_row("0", "Cerrar Sesión")
        
        console.print(table)
        
        opcion = Prompt.ask("Seleccione una opción", choices=["0", "1", "2", "3", "4"])
        
        if opcion == "0":
            console.print("\n[yellow]Cerrando sesión...[/yellow]")
            break
        else:
            console.print(f"\n[bold blue]Función pendiente de implementar: Opción {opcion}[/bold blue]")
            console.input("Presione Enter para continuar...")
            pass

if __name__ == "__main__":
    try:
        getMenu(conn)
    except KeyboardInterrupt:
        console.print("\n[bold red]Programa interrumpido por el usuario[/bold red]")
    except Exception as e:
        console.print(f"\n[bold red]Error: {e}[/bold red]")
