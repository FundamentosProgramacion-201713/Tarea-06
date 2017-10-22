#encoding: utf-8
#Diego Armando Pérez González
#crea un menu para que el usuario pueda utilizar cualquiera de las funciones anteriores


def recolectarInsectos():

    print("Bienvenido al programa que registra los insectos que recolectas")
    print("")

    contadorDias = 0
    acumuladorBichos = 0
    insectos = 30

    while acumuladorBichos < 30:
        dato1 = int(input("¿Cuantos insectos atrapaste hoy?  "))
        contadorDias += 1
        acumuladorBichos += dato1

        if acumuladorBichos > 30:
            print("Después de", contadorDias, "día(s) de recoleción llevas", acumuladorBichos, "insectos")
            print("Te has pasado con", acumuladorBichos - 30, "insectos")
            print("")
            print("¡Felicidades, has llegado a la meta!")
            print("")
            break

        if acumuladorBichos == 30:
            print("Después de", contadorDias, "día(s) de recoleción llevas", acumuladorBichos, "insectos")
            print("Te hace falta recolectar", insectos - 30, "insectos")
            print("")
            print("¡Felicidades, has llegado a la meta!")
            print("")
            break

        print("Después de", contadorDias, "día(s) de recoleción llevas", acumuladorBichos, "insectos")
        print("Te hace falta recolectar", insectos - acumuladorBichos, "insectos")

def encontrarElMayor():

    print("Bienvenido al programa que encuentra el mayor")
    print("")

    numeroInicial = 0
    numeroMayor = [numeroInicial]

    numeroNuevo = int(input("Teclea un número [-1 para salir]:"))
    numeroMayor.append(numeroNuevo) #apoyo isc 5 y ideos de youtube

    while numeroNuevo != -1:
        numeroNuevo = int(input("Teclea un número [-1 para salir]:"))
        numeroMayor.append(numeroNuevo)

    if numeroNuevo == -1:
        print("")
        print("El mayor es:", (max(numeroMayor)))

def main():

    opcion= 0

    while opcion >= 0 or opcion <=0:
        print("Tarea 06. Ciclos while")
        print("Autor: Diego Armando Pérez González")
        print('''
            1. Recolectar insectos
            2. Econtrar el mayor
            3. Salir
            ''')
        opcion = int(input("Teclea tu opción: "))
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        if opcion == 1:
            recolectarInsectos()
            print("")
            print("")

        elif opcion == 2:
            encontrarElMayor()
            print("")
            print("")

        elif opcion == 3:
            print("Gracias por usar este programa, regresa pronto.")
            print("")
            print("")
            break

        else:     #opcion != 1 or opcion!=2 or opcion!=3: (otra opción)
            print("Solo se puede del 1 al 3")
            print("Tarea 06. Ciclos while")
            print("Autor: Diego Armando Pérez González")
            print('''
                1. Recolectar insectos
                2. Econtrar el mayor
                3. Salir
                ''')
            opcion = int(input("Teclea tu opción: "))
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")


main()