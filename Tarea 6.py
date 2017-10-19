#Encoding: UTF-8
#Autor: Luis Daniel Rivera Salinas A01374997
#Tarea 3

def recolectarInsectos():
    print("Bienvenido al programa que registra los insectos \nque recolectas")
    insectos = 0
    dias = 0
    insectosFaltantes = 30
    insectosAtrapados = 0
    while insectos < 30:
        insectos = int(input("¿Cuántos insectos atrapaste hoy? "))
        insectosAtrapados = insectos + insectosAtrapados
        dias += 1

        if insectos >= 30:
            print("Después de ", dias, "dia(s) de recolección, llevas ",insectos,"insectos")
            insectos -= 30
            print("Te has pasado con ",insectos," insectos")
            print("¡Felicidades, has llegado a la meta!")
            insectos = 30

        elif insectos < 30:
            print("Después de ", dias, "dia(s) de recolección, llevas ", insectosAtrapados, "insectos")
            insectosFaltantes = insectosFaltantes - insectos
            if insectosFaltantes > 0:
                print("Te hace falta recolectar ",insectosFaltantes, " insectos")
            elif insectosFaltantes <= 0:
                print("Te hace falta recolectar 0 insectos")
                pasados = insectosAtrapados-30
                print("Te has pasado con ", pasados, " insectos")
                print("¡Felicidades, has llegado a la meta!")
                insectos = 30

def encontrarElMayor():
    lista = []
    print("Bienvenido al programa que encuentra el mayor")
    salir = 1
    intento = 1
    while salir == 1:
        numero = (int(input("Teclea un número [-1 para salir]: ")))

        if numero == -1 and intento == 1:
            print("No hay valor mayor")
            salir = 0

        elif numero > -1 and intento >= 1:
            lista.append(numero)
            intento += 1

        elif numero == -1 and intento > 1:
            print("El mayor es: ",max(lista))
            salir = 0


def main():
    salirMain = 0
    while salirMain == 0:
        print("Tarea 06. Ciclos while \nAutor: Luis Daniel Rivera Salinas ")
        print("     ")
        print("1. Recolectar insectos")
        print("2. Encontrar el mayor")
        print("3. Salir")
        opcion = int(input("Teclea tu opción: "))

        if opcion > 3 or opcion <= 0:
            print("ERROR, teclea 1, 2 o 3")
            print("  ")
            print("  ")
        elif opcion == 1:
            print("  ")
            recolectarInsectos()
            print("  ")
            print("  ")
        elif opcion == 2:
            print("  ")
            encontrarElMayor()
            print("  ")
            print("  ")
        elif opcion == 3:
            print("Gracias por usar este programa, regresa pronto.")
            salirMain = 1

main()