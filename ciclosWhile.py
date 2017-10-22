#encoding: UTF-8
#Autor: Daniel Sahuer
#Programa que mediante un menú, se registran insectos recolectados o se encuentra el número mayor de un conjunto


def recolectarInsectos(): #Calcula cuantos insectos faltan para llegar a la meta y cuantos se han recolectado por día. Sí se pasa de la meta, avisa por cuanto se pasó.
    dias = 0
    cuenta = 0
    total = 0

    while cuenta < 30:
        dias +=1
        insectos = int(input("¿Cuántos insectos atrapaste hoy? "))
        cuenta = cuenta + insectos
        total = 30 - cuenta

        if cuenta <= 30:
            print("Después de %d día(s) de recolección, llevas %d insectos" % (dias,cuenta))
            print("Te hace falta recolectar %d insectos" % total)

        elif cuenta > 30:
            print("Después de %d día(s) de recolección, llevas %d insectos" % (dias, cuenta))
            print("Te has pasado con %d insectos" % -total)

    print("¡Felicidades, has llegado a la meta!")


def encontarMayor(): #Calcula el número mayor de un conjunto de números positivos, el conjunto y el programa terminan si se escribe -1.
    lista= []
    dato = int(input("Teclea un número [-1 para salir]: "))

    while dato != -1:
        lista.append(dato)
        dato = int(input("Teclea un número [-1 para salir]: "))

    if len(lista) > 0:
        print("El mayor es: ", max(lista))
    else:
        print("No hay valor mayor")


def main():

    opcion = 0
    while opcion != 3:
        print("\nTarea 06. Ciclos while\nAutor: Daniel Sahuer\n\n1. Recolectar insectos\n2. Encontrar el mayor\n3. Salir\n")
        opcion = int(input("Teclea tu opción: "))

        if opcion == 1:
            print("Bienvenido al programa que registra los insectos que recolectas")
            recolectarInsectos()
        elif opcion == 2:
            encontarMayor()
        elif opcion == 3:
            print("Gracias por usar este programa, regresa pronto.")
        else:
            print("ERROR, teclea 1, 2 o 3")


main()