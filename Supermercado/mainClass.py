from Transporte import Transporte
from Tecnologia import Tecnologia
from Tv import Tv



def registrarArticulo():
    op = "0"
    print("¿Qué desea registrar?")
    print("1 para TV")
    print("2 para Consola")
    print("3 para Scooter")
    print("4 para Bicicleta")
    if op ==1:
        registrarTv()
    if op ==2:
        registrarConsola()
    if op ==3:
            registrarScooter()
    if op ==4:
        registrarBicicleta()

def cotizarArticulo():
    op = "0"
    print("¿Qué desea Cotizar?")
    print("1 para TV")
    print("2 para Consola")
    print("3 para Scooter")
    print("4 para Bicicleta")
    if op ==1:
        cotizarTv()
    if op ==2:
        cotizarConsola()
    if op ==3:
        cotizarScooter()
    if op ==4:
        cotizarBicicleta()

def registrarTv():
    print("REGISTRAR TV")
    marca = str(input("¿Qué marca es la Tv?"))
    voltaje = int(input("¿Cuál es el voltaje?"))
    eficiencia = str(input("Indique la eficiencia A-B-C-E-F"))
    precio = float(input("¿Cuál es el precio de la Tv?"))
    tamanio = float(input("¿Cuál es el tamaño de la Tv?"))
    t = Tv((voltaje,precio,eficiencia,marca,tamanio))

def registrarConsola():
            pass
def registrarScooter():
            pass
def registrarBicicleta():
            pass

def cotizarTv():
    print("TELEVISORES")

            
def cotizarConsola():
            pass
def cotizarScooter():
            pass
def cotizarBicicleta():
            pass


opcion = "o"
while opcion!= "o":
    print("BIENVENIDO")
    print("¿Que desea hacer?")
    print("1 registrar un articulo")
    print("2 Cotizar un articulo")
    print("presione o para detener programa")
    opcion = input("ingrese una opcion")
    if opcion =="1":
        registrarArticulo(int(opcion))
    elif opcion =="2":
        cotizarArticulo(int(opcion))
    elif opcion.lower()=="o":
        print("Hasta luego")
    else:
        print("Ingrese una opción válida")