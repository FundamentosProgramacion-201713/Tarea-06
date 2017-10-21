#encode UTF-8
#AUTOR: Luis Enrique Neri Pérez
#MATRÍCULA: A01745995
#DESCRIPCIÓN: Un menú que despliegue dos funciones y cuando el usuario desee puede salirse del menú.

def recolectarInsectos():
    print("\n")
    print("RECOLECTOR DE INSECTOS")
    print("-----------------------------")
    print("Bienvenido al programa que registra los insectos que recolectas")
    recolectado = 0
    dia = 0
    while not recolectado >= 30:
        print("\n")
        recolectado = recolectado +  int(input("¿Cuántos insectos atrapaste hoy?: "))
        dia = dia + 1
        falta = 30 - recolectado
        print("Tras %d día(s) de recolección llevas %d insectos recolectados" % (dia, recolectado))
        if recolectado<30:
            print("Te hace falta recolectar %d insecto(s)" % falta)
    if recolectado>30:
        recolectado = recolectado - 30
        print("-----------------------------------------------------------")
        print("¡FELICIDADES HAS REBAZADO TU META CON %d INSECTO(S) DE MÁS!" % recolectado)
        print("-----------------------------------------------------------")
    else:
        print("-----------------------------------------------------------")
        print("¡FELICIDADES HAS LLEGADO A TU META!")
        print("-----------------------------------------------------------")


def encontrarMayor():
    print("\n")
    print("ENCONTRAR EL MAYOR")
    print("-----------------------------")
    print("Bienvenido al programa para encontrar al número mayor:")
    lista = []
    dato = int(input("Teclea un número [-1 para salir]:"))
    if dato != -1:
        while not dato==-1:
            lista.append(dato)
            dato = int(input("Teclea un número [-1 para salir]:"))
        maximo = max(lista)
        print("------------------------------")
        print("EL MAYOR ES:", maximo)
        print("------------------------------")
    else:
        print("------------------------------")
        print("NO SE INGRESARON DATOS")



def main():
    print("TAREA 06: Ciclos While")
    print("-----------------------------")
    print("01. Recolectar Insectos")
    print("02. Encontrar el Mayor")
    print("03. Salir")
    opcion = int(input("TECLEE SU OPCIÓN: "))
    while not opcion == 3:
        if opcion == 1:
            recolectarInsectos()
        elif opcion == 2:
            encontrarMayor()
        else:
            print("ERROR. Escriba únicamente 1 o 2 o 3")
        print("\n")
        print("TAREA 06: Ciclos While")
        print("-----------------------------")
        print("01. Recolectar Insectos")
        print("02. Encontrar el Mayor")
        print("03. Salir")
        opcion = int(input("TECLEE SU OPCIÓN: "))

    print("\n")
    print("GRACIAS POR USAR ESTE PROGRAMA ¡HASTA PRONTO!")


main()