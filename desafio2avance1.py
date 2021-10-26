#Lucas Ramírez, Boris Aguilar
#Desafio 2

#se crea la función menú
def menu():
    print("__MENÚ PRINCIPAL__")
    print("Escoja una opción:")
    print("1: Generar estado incial del puerto seco")
    print("2: Imprimir estado del puerto seco")
    print("3: Ubicar un contenedor")
    print("4: Incluir un nuevo contenedor")
    print("5: Retirar un contenedor")
    print("0: Cerrar jornada laboral")
    opcion = int(input())
    return opcion

def opc1():
    print("GENERAR ESTADO INICIAL DEL PUERTO SECO")
    m = int(input("Ingrese la cantidad máxima de pilas de contenedores"))
    n = int(input("Ingrese la cantidad máxima de contenedores en una pila"))
    print("Cantidad máxima de pilas:" ,m)
    print("Cantidad máxima de contenedores apilados:" ,n)
    return m,n
    
###FUNCION PRINCIPAL###

opcion = menu()
if opcion == 1:
    opc1()
    
    