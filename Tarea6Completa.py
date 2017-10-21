#UTF-8
#Natalia Meraz Tostado
#Tarea 6 ciclos while
import sys

def contarInsectos():
    insectos = int(input("¿Cuántos insectos atrapaste hoy?: "))
    total = insectos
    while total <= 30 or total >= 30:

        for x in range(1,100,1):
            faltantes = 30 - total
            print("Después de", x, "dia(s) de recolección, llevas", total, "insectos")

            if faltantes < 30 and faltantes > 0:
                print("Te hace falta recolectar", faltantes, "insectos")
                nuevos = int(input("¿Cuántos insectos atrapaste hoy?: "))
                total = total + nuevos
            elif total == 30:
                print("¡Felicidades, has llegado a la meta!")
                break
            elif total > 30:
                print("Te has pasasdo con", (faltantes*-1), "insectos")
                print("¡Felicidades, has llegado a la meta!")
        break


def esMayorOMenor():
    lista = []
    dato = int(input("Teclea un valor [-1 para salir]: "))
    while dato != -1:
        lista.append(dato)
        dato = int(input("Teclea un valor [-1 para salir]: "))

    if len(lista) > 0:
        print("El mayor es: ", max(lista))

    else:
        print("No hay valor mayor")


def main():
    print("1. Recolectar insectos")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))
    while opcion != 3:

        if opcion == 1:
            print("Bienvenido al programa que registra los insectos que recolectas")
            contarInsectos()

        elif opcion == 2:
            print("Bienvenido al programa que encuentra el mayor")
            esMayorOMenor()

        elif opcion == 3:
            print("Gracias por usar este programa, regresa pronto")
            sys.exit(0)

        else:
            print("ERROR, teclea 1, 2 o 3")

        print("1. Recolectar insectos")
        print("2. Encontrar el mayor")
        print("3. Salir")
        opcion = int(input("Teclea tu opción: "))



main()