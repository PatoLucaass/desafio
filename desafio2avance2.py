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

#opción 1
def opc1():
    print("GENERAR ESTADO INICIAL DEL PUERTO SECO")
    M = int(input("Ingrese la cantidad máxima de pilas de contenedores: " ))
    N = int(input("Ingrese la cantidad máxima de contenedores en una pila: "))
    puerto = []

    if N==M or N<M: # dejamos la ultima fila vacía
		
        for i in range(M):
            contenedores = []
            for j in range(N):
                contenedores.append(input("Ingrese numero/NombreEmpresa: "))
            contenedores.append(0) # valor 0 representa espacio vacío
            puerto.append(contenedores)
		
    else: # dejamos la ultima fila vacía + 1 elmento
		
        for i in range(M):
            contenedores = []
            for j in range(N):
                if i == 0 and j == N-1:
                    contenedores.append(0) # valor 0 representa espacio vacío
                else:
                    contenedores.append(input("Ingrese numero/NombreEmpresa: "))	
            contenedores.append(0) # valor 0 representa espacio vacío
            puerto.append(contenedores)
    return puerto, N, M

#opcion 2
def opc2(puerto, N, M):
    print("IMPRIMIR ESTADO DEL PUERTO SECO")
    i = N-1
    while (i >= 0):
        j = M-1
        print("| ", end = " ")
        while (j >= 0):
            print (puerto[j][i], " | ", end=" ")
            j = j - 1
        print("")
        i = i - 1
    
###FUNCION PRINCIPAL###


opcion = menu()
while opcion != 0:
    if opcion == 1:
        puerto, N, M = opc1()
        opcion = menu()
    if opcion == 2:
        opc2(puerto, N+1, M)
        opcion = menu()
