# Realiza un menu iterativo
# Cada opcion debe ser una funcion => fz()
# Opcion 1 : Sumar 2 numeros
# Opcion 2 : Crea una coleccion de productos para un mercado
# Opcion 3 : Agrega un nuevo producto a la coleccion
# Opcion 4 : Mostrar el producto de precio mas bajo
# Opcion 5 : Salir
import os
coleccion=[]
def suma():
    try:
        print("Suma de 2 numero")
        n_1=int(input("ingresa un numero: "))
        n_2=int(input("ingresa otro numero: "))
        print(f"suma = {n_1+n_2}")
    except ValueError as e:
        print(e)
#======================================================
def crearColeccionProductos():
    global coleccion
    print("Crear una nueva coleccion de productos")
    n=int(input("cuentos productos se van a crear: "))
    for i in range(n):
        name=input(f"Nombre del producto {i+1}: ")
        price=float(input(f"precio del producto {i+1}: "))
        coleccion.append({"Nombre":name,"Precio":price})
        print(f"agregado correctamente\n")
    print(f"--COLECCION--")
    mostrarColeccion(coleccion)
#======================================================
def agregarColeccionProductos():
    global coleccion
    large=len(coleccion)
    print("Agregar un nuevo producto")
    name=input(f"Nombre del producto {large+1}: ")
    price=float(input(f"precio del producto {large+1}: "))
    coleccion.append({"Nombre":name,"Precio":price})
    print(f"agregado correctamente\n\n--COLECCION--")
    mostrarColeccion(coleccion)
#======================================================
def precioMasBajo():
    global coleccion
    print("Mostrar el producto con el precio mas bajo")
    if not coleccion:
        print("Vacio")
        return
    priceMin=min(precio["Precio"] for precio in coleccion)
    repeticion=[precio for precio in coleccion if precio["Precio"]==priceMin]
    if repeticion==1: print(f"el precio mas bajo es:'{priceMin['Nombre']}' con {priceMin['Precio']}")
    else: 
        print(f"\nexiste mas de un procucto con precio minimo")
        mostrarColeccion(repeticion)
#======================================================
def mostrarColeccion(coleccion):
    for producto in coleccion:
            print(f"{producto['Nombre']} : {producto['Precio']}")
#======================================================
def MENU():
    band=True
    while band:
        pantalla="""
                .: MENU :.        
            Opcion 1 : Sumar 2 numeros
            Opcion 2 : Crea una coleccion de productos para un mercado
            Opcion 3 : Agrega un nuevo producto a la coleccion
            Opcion 4 : Mostrar el producto de precio mas bajo
            Opcion 5 : Salir        
        """
        print(pantalla)
        op=int(input("ingrese su opcion: "))
        print()
        match op:
            case 1: 
                suma()
                print(input("continuar[ENTER]"))
                os.system("ls")
            case 2: 
                crearColeccionProductos()
                print(input("continuar[ENTER]"))
                os.system("ls")
            case 3: 
                agregarColeccionProductos()
                print(input("continuar[ENTER]"))
                os.system("ls")
            case 4: 
                precioMasBajo()
                print(input("continuar[ENTER]"))
                os.system("ls")
            case 5: 
                    band=False
                    print("hasta luego! <°^°>/ ")
            case _: print("opcion no valida")
MENU()