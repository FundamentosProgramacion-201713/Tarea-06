# encoding: UTF-8
# Autor: Siham El Khoury Caviedes, A01374764.

# Menú de las funciones de la Tarea 06.

def recolectarInsectos():
    insectos = 0
    dias = 0
    print("Bienvenido al programa que registra los insectos que recolectas")

    while insectos < 30:
        numero = int(input("¿Cuántos insectos recuperaste hoy? "))
        dias = dias + 1
        insectos = insectos + numero
        print("Después de %d día(s) de recolección, llevas %d insectos" % (dias, insectos))

        if insectos <= 30:
            faltantes = 30 - insectos
            print("Te hace falta recolectar %d insectos" % faltantes)
        else:
            pasados = insectos - 30
            print("Te has pasado con %d insectos" % pasados)

        if insectos >= 30:
            print("¡Felicidades, has llegado a la meta!")


def encontrarMayor():
    print("Bienvenido al programa que encuentra el mayor")
    lista = []
    numero = int(input("Teclea un número [-1 para salir]: "))

    while numero != -1:
        lista.append(numero)
        numero = int(input("Teclea un número [-1 para salir]: "))

    if lista == []:
        print("No hay valor mayor")
    else:
        maximo = max(lista)
        print("El mayor es: %d" % maximo)


def main():
    opcion = 0

    while opcion != 3:
        print("Tarea 06. Ciclos while")
        print("Autor: Siham El Khoury Caviedes")
        print()
        print("1. Recolectar insectos")
        print("2. Encontrar el mayor")
        print("3. Salir")
        opcion = int(input("Teclea tu opción: "))

        if opcion == 1:
            print()
            recolectarInsectos()
            print()
            print()

        elif opcion == 2:
            print()
            encontrarMayor()
            print()
            print()

        elif opcion != 3:
            print()
            print("Opción inválida. Por favor, vuelve a intentarlo.")
            print()
            print()


main()
