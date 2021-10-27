#Lucas Ramírez, Boris Aguilar
#Desafio 2

from random import randint

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

#se crea la respuesta a la opción 1
def opc1():
    print("GENERAR ESTADO INICIAL DEL PUERTO SECO")
    m = int(input("Ingrese la cantidad máxima de pilas de contenedores"))
    n = int(input("Ingrese la cantidad máxima de contenedores en una pila"))
    print("Cantidad máxima de pilas:" ,m)
    print("Cantidad máxima de contenedores apilados:" ,n)
    
    '''pilas = []
    for i in range(m):
	    pila1 = []
	    p1=randint(1,n)
	    for j in range(p1):
	    	pila1.append()
	    pilas.append(pila1)
    print(pilas)'''
    
    return m,n
    
###FUNCION PRINCIPAL###

opcion = menu()
if opcion == 1:
    opc1()
    
    

    
    