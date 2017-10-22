#Encoding: UTF-8
#Autor: Alberto López Reyes
#Descripción: Este programa mantiene un registro de insectos
#para completar el objetivo de recolectar 30 y encuentra el valor mayor de una serie de números otorgados.

import sys

strAutor = "Alberto López Reyes"

def diferenciaInsectos(insectosHoy):
    intDiferenciaInsectos = 30 - insectosHoy
    return intDiferenciaInsectos

def diferenciaInsectos2(insectosTotales):
    intDiferenciaInsectos2 = insectosTotales - 30
    return intDiferenciaInsectos2

def objetivoInsectos():
    print("""
Bienvenido al programa que registra los insectos
que recolectas""")

    intNumInsectos = 0
    intNumDias = 0

    while intNumInsectos < 30:
        intNumInsectosHoy = int(input("""¿Cuántos insectos atrpaste hoy? """))
        intNumInsectos = intNumInsectos + intNumInsectosHoy

        intDiferenciaInsectos = diferenciaInsectos(intNumInsectos)

        intNumDias = intNumDias + 1

        print("""Después de """+str(intNumDias)+""" día(s) de recolección, llevas """
+str(intNumInsectos)+""" insectos""")

        if intNumInsectos > 30:
            intDiferenciaInsectos2 = diferenciaInsectos2(intNumInsectos)

            print("Te has pasado con "+str(intDiferenciaInsectos2)+" insectos.")

        else:
            print("Te hace falta recolectar: "+str(intDiferenciaInsectos)+" insectos")

    print("""¡Felicidades, has llegado a la meta!
""")

    main()

def maximoLista():
    print("""
Bienvenido al programa que encuentra el mayor""")

    lstValores = []

    intVeces = 0
    intValor = 0

    while intValor != -1:
        intValor = int(input("Teclea un número [-1 para salir]: "))
        lstValores.append(intValor)
        intVeces = intVeces + 1

    if intVeces == 1:
        print("""No hay valor mayor
""")

    else:
        print("El mayor es: "+str(max(lstValores))+"""
""")

    main()

def error():
    print("""ERROR, teclea 1, 2 o 3
""")

    main()

def main():
    print("Tarea 06. Ciclos while")
    print("Autor: "+strAutor)

    print("""
1. Recolectar insectos
2. Encontrar el mayor
3. Salir
""")

    intSeleccion = int(input("Teclea tu opción: "))

    while intSeleccion >= 1 and intSeleccion <= 3:
        if intSeleccion == 1:
            objetivoInsectos()

        elif intSeleccion == 2:
            maximoLista()

        elif intSeleccion == 3:
            print("""Gracias por usar este programa, regresa pronto.""")
            sys.exit()

    error()

main()
