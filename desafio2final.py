# Lucas Ramírez, Boris Aguilar
# Desafio 2

from random import randint


# se crea la función menú
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


# opción 1
def opc1():
    print("GENERAR ESTADO INICIAL DEL PUERTO SECO")
    M = int(input("Ingrese la cantidad máxima de pilas de contenedores: "))
    N = int(input("Ingrese la cantidad máxima de contenedores en una pila: "))
    puerto = []

    if N == M or N < M:  # dejamos la ultima fila vacía

        for i in range(M):
            contenedores = []
            for j in range(N):
                contenedores.append(input("Ingrese numero/NombreEmpresa: "))
            contenedores.append(0)  #0 representa espacio vacío
            puerto.append(contenedores)

    else:  #ultima fila vacía mas 1 elmento

        for i in range(M):
            contenedores = []
            for j in range(N):
                if i == 0 and j == N - 1:
                    contenedores.append(0)  # valor 0 representa espacio vacío
                else:
                    contenedores.append(input("Ingrese numero/NombreEmpresa: "))
            contenedores.append(0)  # valor 0 representa espacio vacío
            puerto.append(contenedores)
    return puerto, N, M


# opcion 2
def opc2(puerto, N, M):
    print("IMPRIMIR ESTADO DEL PUERTO SECO")
    i = N - 1
    while (i >= 0):
        j = M - 1
        print("| ", end=" ")
        while (j >= 0):
            print(puerto[j][i], " | ", end=" ")
            j = j - 1
        print("")
        i = i - 1


# opcion 3
def opc3(puerto):
    contenedor = input("Ingrese numero/NombreEmpresa del contenedor a buscar: ")

    a, b = buscar(puerto, contenedor)
    if (a == -1 and b == -1):
        imprimepuerto(puerto, N, M)
        print("Contenedor no se encuentra en el puerto")
    else:
        imprimepuerto(puerto, N, M)
        print("\nEl contenedor buscado ", contenedor, ", se encuentra en la pila ", M - a, " en el nivel ", b + 1)

# opcion 4
def opc4(puerto, N, M):
    if capacidadpuerto(puerto, N, M) == 0:
        print("El puerto está lleno. No podemos recibir su contenedor ")
    else:
        i = 0
        while (i < M):
            j = 0
            while (j < N):
                if puerto[i][j] == 0:  #Espacio vacio
                    puerto[i][j] = input("Ingrese numero/NombreEmpresa de contenedor a agregar: ")
                    imprimepuerto(puerto, N, M)
                    return puerto
                j = j + 1
            i = i + 1
    return puerto

# opcion 5
def opc5(puerto, N, M):
    contenedor = input("Ingrese numero/NombreEmpresa del contenedor a quitar: ")
    a, b = buscar(puerto, contenedor)
    print(N, M, a, b)

    if (b + 1 == N):
        print("Puedo retirar contenedor")  # puerto[a][b] = 0
        puerto.remove(contenedor)
        return puerto
    elif capacidadpuerto(puerto, N, M) == 0:
        print("No puedo retirar contenedor")
        return puerto

    if (puerto[a][b + 1] == 0):
        print("Puedo retirar contenedor")  # puerto[a][b] = 0
        puerto.remove(contenedor)
        return puerto
    else:
        print("Debo hacer los cambios para retirar contenedor")
        # sumar instrucciones para hacer los cambios
    return puerto


def capacidadpuerto(puerto, N, M):
    if N == M or N < M:
        vacios = N
    else:
        vacios = N + M - 1

    capacidad = (N + 1) * (M) - vacios

    for pilas in puerto:
        for contenedor in pilas:
            if contenedor != 0:
                capacidad = capacidad - 1

    return capacidad


def imprimepuerto(puerto, N, M):
    i = N
    print("\n\n\n")
    while (i >= 0):
        j = M - 1
        print("| ", end=" ")
        while (j >= 0):
            print(puerto[j][i], " | ", end=" ")
            j = j - 1
        print("")
        i = i - 1


def buscar(puerto, contenedor):
    index = -1 
    i = 0
    while (i < len(puerto)): 

        if puerto[i].count(contenedor) > 0:  
            index = puerto[i].index(contenedor)
            pilak = i
        i = i + 1
    if index != -1:
        return (pilak, index)
    else:
        return (-1, -1)


###FUNCION PRINCIPAL###

# opcion = menu()

opcion = menu()
while opcion != 0 and opcion < 6:
        if opcion == 1:
            puerto, N, M = opc1()
        elif opcion == 2:
            opc2(puerto, N + 1, M)
        elif opcion == 3:
            print(opc3(puerto))
        elif opcion == 4:
            print(opc4(puerto, N, M))
        elif opcion == 5:
            opc5(puerto, N, M)
        opcion = menu()
print("Ha terminado su jornada laboral.")
