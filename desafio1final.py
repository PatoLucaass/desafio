#Desafio 1 Taller de Ingenieria II
#Lucas Ramirez y Boris Aguilar

from random import randint
##########################
#Se generan las 16 variables y se les asigna un numero al azar entre 1 y 4
cua1 = randint(1,4)
cua2 = randint(1,4)
cua3 = randint(1,4)
cua4 = randint(1,4)
cua5 = randint(1,4)
cua6 = randint(1,4)
cua7 = randint(1,4)
cua8 = randint(1,4)
cua9 = randint(1,4)
cua10 = randint(1,4)
cua11 = randint(1,4)
cua12 = randint(1,4)
cua13 = randint(1,4)
cua14 = randint(1,4)
cua15 = randint(1,4)
cua16 = randint(1,4)
####################
#Se identifica el numero generado y se le asigna un elemento dependiendo del numero. 1 = P, 2 = A y 3 o 4 = B
if cua1 == 1:
    A1 = "P"
elif cua1 == 2:
    A1 = "A"
else:
    A1 = "B"
################   
if cua2 == 1:
    A2 = "P"
elif cua2 == 2:
    A2 = "A"
else:
    A2 = "B"
################
if cua3 == 1:
    A3 = "P"
elif cua3 == 2:
    A3 = "A"
else:
    A3 = "B"
################
if cua4 == 1:
    A4 = "P"
elif cua4 == 2:
    A4 = "A"
else:
    A4 = "B"
################
if cua5 == 1:
    B1 = "P"
elif cua5 == 2:
    B1 = "A"
else:
    B1 = "B"
################
if cua6 == 1:
    B2 = "P"
elif cua6 == 2:
    B2 = "A"
else:
    B2 = "B"
################
if cua7 == 1:
    B3 = "P"
elif cua7 == 2:
    B3 = "A"
else:
    B3 = "B"
################
if cua8 == 1:
    B4 = "P"
elif cua8 == 2:
    B4 = "A"
else:
    B4 = "B"
################
if cua9 == 1:
    C1 = "P"
elif cua9 == 2:
    C1 = "A"
else:
    C1 = "B"
################
if cua10 == 1:
    C2 = "P"
elif cua10 == 2:
    C2 = "A"
else:
    C2 = "B"
################
if cua11 == 1:
    C3 = "P"
elif cua11 == 2:
    C3 = "A"
else:
    C3 = "B"
################
if cua12 == 1:
    C4 = "P"
elif cua12 == 2:
    C4 = "A"
else:
    C4 = "B"
################
if cua13 == 1:
    D1 = "P"
elif cua13 == 2:
    D1 = "A"
else:
    D1 = "B"
################
if cua14 == 1:
    D2 = "P"
elif cua14 == 2:
    D2 = "A"
else:
    D2 = "B"
################
if cua15 == 1:
    D3 = "P"
elif cua15 == 2:
    D3 = "A"
else:
    D3 = "B"
################
if cua16 == 1:
    D4 = "P"
elif cua16 == 2:
    D4 = "A"
else:
    D4 = "B"
################
#Se imprime como cuadrante
print("-----------------")
print("|",A1,"|",B1,"|",C1,"|",D1,"|")
print("-----------------")
print("|",A2,"|",B2,"|",C2,"|",D2,"|")
print("-----------------")
print("|",A3,"|",B3,"|",C3,"|",D3,"|")
print("-----------------")
print("|",A4,"|",B4,"|",C4,"|",D4,"|")
print("-----------------")
######################################
#Se generan 2 variables para empezar el conteo de las especies
conteoP = 0 
conteoB = 0 
#########################
if A1 == "P":
    conteoP = conteoP + 1
elif A1 == "B":
    conteoB = conteoB + 1
#########################
if A2 == "P":
    conteoP = conteoP + 1
elif A2 == "B":
    conteoB = conteoB + 1
#########################
if A3 == "P":
    conteoP = conteoP + 1
elif A3 == "B":
    conteoB = conteoB + 1
#########################
if A4 == "P":
    conteoP = conteoP + 1
elif A4 == "B":
    conteoB = conteoB + 1
#########################
if B1 == "P":
    conteoP = conteoP + 1
elif B1 == "B":
    conteoB = conteoB + 1
#########################
if B2 == "P":
    conteoP = conteoP + 1
elif B2 == "B":
    conteoB = conteoB + 1
#########################
if B3 == "P":
    conteoP = conteoP + 1
elif B3 == "B":
    conteoB = conteoB + 1
#########################
if B4 == "P":
    conteoP = conteoP + 1
elif B4 == "B":
    conteoB = conteoB + 1
#########################
if C1 == "P":
    conteoP = conteoP + 1
elif C1 == "B":
    conteoB = conteoB + 1
#########################
if C2 == "P":
    conteoP = conteoP + 1
elif C2 == "B":
    conteoB = conteoB + 1
#########################
if C3 == "P":
    conteoP = conteoP + 1
elif C3 == "B":
    conteoB = conteoB + 1
#########################
if C4 == "P":
    conteoP = conteoP + 1
elif C4 == "B":
    conteoB = conteoB + 1
#########################
if D1 == "P":
    conteoP = conteoP + 1
elif D1 == "B":
    conteoB = conteoB + 1
#########################
if D2 == "P":
    conteoP = conteoP + 1
elif D2 == "B":
    conteoB = conteoB + 1
#########################
if D3 == "P":
    conteoP = conteoP + 1
elif D3 == "B":
    conteoB = conteoB + 1
#########################
if D4 == "P":
    conteoP = conteoP + 1
elif D4 == "B":
    conteoB = conteoB + 1
#########################
conteoA = 16 - conteoP - conteoB
#########################
porceP = (conteoP/16)*100
porceB = (conteoB/16)*100
#########################
#Se imprimen las cantidades y porcentajes
print("La cantidad de agua es:",conteoA)
print("La cantidad de plantas es:",conteoP)
print("El porcentaje de plantas es:",round(porceP),"%")
print("La cantidad de bacterias es:",conteoB)
print("El porcentaje de bacterias es:",round(porceB),"%")
print( )
##########################################################
#Se consulta por el elemento con mayor ocurrencia y/o si la cantidad de plantas y bacterias empatan
if conteoP>conteoB and conteoP>conteoA:
    print("El elemento que más se repite son plantas.")
elif conteoB>conteoP and conteoB>conteoA:
    print("El elemento que más se repite son bacterias.")
elif conteoA>conteoP and conteoA>conteoB:
    print("El elemento que más se repite es el agua.")
if conteoP==conteoB and conteoP==conteoA:
    print("La cantidad de plantas, bacterias y agua es la misma.")
elif conteoP==conteoB:
    print("La cantidad de plantas y bacterias es la misma.")
elif conteoP==conteoA:
    print("La cantidad de plantas y agua es la misma.")
elif conteoA==conteoB:
    print("La cantidad de agua y bacterias es la misma.")
##########################################################
#Se consulta por la existencia de las relaciones entregadas en el Desafio
if B2=="P" and A1=="B" and A2=="B" and A3=="B" and B1=="B" and B3=="B" and C1=="B" and C2=="B" and C3=="B":
    print ("En la posición B2 hay una relación Planta-Bajo-Ataque.")
elif B3=="P" and A2=="B" and A3=="B" and A4=="B" and B2=="B" and B4=="B" and C2=="B" and C3=="B" and C4=="B":
    print ("En la posición B3 hay una relación Planta-Bajo-Ataque.")
elif C2=="P" and B1=="B" and B2=="B" and B3=="B" and C1=="B" and C3=="B" and D1=="B" and D2=="B" and D3=="B":
    print ("En la posición C2 hay una relación Planta-Bajo-Ataque.")
elif C3=="P" and B2=="B" and B3=="B" and B4=="B" and C2=="B" and C4=="B" and D2=="B" and D3=="B" and D4=="B":
    print ("En la posición C3 hay una relación Planta-Bajo-Ataque.")
#############################################################################################################
if B2=="A" and A1=="P" and A2=="P" and A3=="P" and B1=="P" and B3=="P" and C1=="P" and C2=="P" and C3=="P":
    print ("En la posición B2 hay una relación Agua-Riesgo-Escasez.")
elif B3=="A" and A2=="P" and A3=="P" and A4=="P" and B2=="P" and B4=="P" and C2=="P" and C3=="P" and C4=="P":
    print ("En la posición B3 hay una relación Agua-Riesgo-Escasez.")
elif C2=="A" and B1=="P" and B2=="P" and B3=="P" and C1=="P" and C3=="P" and D1=="P" and D2=="P" and D3=="P":
    print ("En la posición C2 hay una relación Agua-Riesgo-Escasez.")
elif C3=="A" and B2=="P" and B3=="P" and B4=="P" and C2=="P" and C4=="P" and D2=="P" and D3=="P" and D4=="P":
    print ("En la posición C3 hay una relación Agua-Riesgo-Escasez.")