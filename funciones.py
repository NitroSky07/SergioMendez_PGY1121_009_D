import numpy as np
np.zeros((10,10))
def ver_menu():
    while True:
        print("""MENÚ
        1. Comprar entradas
        2. Mostrar ubicaciones disponibles
        3. Ver listado de asistentes
        4. Mostrar ganancias totales
        5. Salir""")
        break

def validar_opcion():
    try:
        opcion = int(input("Ingrese opcion: "))
        if opcion in(1,2,3,4,5):
            return opcion
        else:
            print("ERROR! OPCION INCORRECTA!")
    except:
        print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_rut():
    while True:
        try:
            rut= int(input("Ingrese rut(sin puntos ni dígito verificador):"))
            if rut >=10000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! EL RUT DEBE DE ESTAR ENTRE 10000000 Y 999999999")
        except:
            print("ERROR! DEBE INGRESAR NÚMERO ENTERO!")

def comprar_entradas():
    while True:
        try:
            cant_entradas == int(input("Ingrese la cantidad de entradas:"))
            if cant_entradas >=1 and cant_entradas <= 3:
                return cant_entradas
            else:
                print("ERROR! LA CANTIDAD DE ENTRADAS DEBE SER 1 o 3!")
        except:
                print("ERROR DEBE INGRESAR UN NÚMERO ENTERO")
        while True:
            print("""PRECIO ENTRADAS
            - Platinum $120.000. (Asientos del 1 al 20).
            - Gold     $80.000.  (Asientos del 21 al 50).
            - Silver   $50.000.  (Asientos del 51 al 100).""")
            comprar_entradas= input("Ingrese que entrada desea: ")
            if comprar_entradas == ("Platinum" or "Gold" or "Silver"):
                return comprar_entradas
            else:
                print("ERROR! LA ENTRADA DEBE SER PLATINUM-GOLD-SILVER!")

def cant_entradas():
    while True:
            try:
                cant_entradas == int(input("Ingrese la cantidad de entradas:"))
                if cant_entradas >=1 and cant_entradas <= 3:
                    return cant_entradas
            except:
                print("ERROR DEBE INGRESAR UN NÚMERO ENTERO")


lista_ruts=[]
lista_filas =[]
lista_columnas =[]
def mostrar_ubicaciones():
    while True:
        print(ver_escenario)
        return mostrar_ubicaciones

def ver_listado():
    while True:
        print()

def ver_escenario():
    for x in range (10):
        print(f"Fila {x+1}: ", end=("  "))
        for y in range(10):
            print(f"Columnas" [x][y], end=(" "))
            print()
        print("Columnas  1 2 3 4 5 6 7 8 9 10")
