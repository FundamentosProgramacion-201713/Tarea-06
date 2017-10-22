#encoding: UTF-8
#Autor: Neftalí Rodríguez Martínez.
#Se incluye una función para contador de insectos y otra función que encuentra el mayor de un grupo de números.


def contarInsectos(): #cuenta el total de insectos atrapados.
    print("Bienvenido al programa que registra los insectos que recolectas")
    print("Recuerda que como mínimo debes de atrapar 30 insectos") #Comentario adicional para el usuario.

    dias = 0
    acumulador_insectos = 0

    while acumulador_insectos < 30:
        insectos = int(input("¿Cuántos insectos atrapaste hoy?: "))
        acumulador_insectos = insectos + acumulador_insectos
        dias = dias + 1

        if  acumulador_insectos < 0:
            print("ERROR, introduce números positivos")
            acumulador_insectos = 0
            dias = 0

        elif acumulador_insectos < 30:
            print("Después de", dias, "día(s) de recolección, llevas", acumulador_insectos, "insectos")
            insectos_faltantes = 30 - acumulador_insectos
            print("Te hace falta recolectar", insectos_faltantes, "insectos")

        elif acumulador_insectos == 30:
            print("Después de", dias, "día(s) de recolección, llevas", acumulador_insectos, "insectos")
            insectos_faltantes = 30 - acumulador_insectos
            print("Te hace falta recolectar", insectos_faltantes, "insectos")
            print("¡Felicidades, has llegado a la meta!")
            print("\r")


        elif acumulador_insectos > 30:
            print("Después de", dias, "día(s) de recolección, llevas", acumulador_insectos, "insectos")
            insectos_excedentes = acumulador_insectos - 30
            print("Te has pasado con", insectos_excedentes,"insectos")
            print("¡Felicidades, has llegado a la meta!")
            print("\r")


def encontrarMayor(): #encuentra el mayor de un conjunto de numeros
    print("Bienvenido al programa que encuentra el mayor")
    numero = 0
    lista = []

    while numero != -1:
        numero = int(input("Teclea un número [-1 para salir]: "))
        if numero > -1:
            lista.append(numero)

    if numero == -1 and lista == []:
        print("No hay valor mayor")
        print("\r")


    elif numero == -1:
        numero_mayor = max(lista)
        print("El mayor es: ", numero_mayor)
        print("\r")


def main (): #programa principal.

    print("Tarea 06. Ciclos While")
    print("Autor: Neftalí Rodríguez Martínez")
    print("\r")

    opcion = 0
    while opcion != 3:
        print("¿Qué quieres hacer?") #Mensaje adicional al usuario.
        print("1. Recolectar insectos") #Sería mejor que la opción se llame CONTAR INSECTOS.
        print("2. Encontrar el mayor")
        print("3. Salir")
        opcion = int(input("Teclea tu opción: "))

        if opcion == 3:
            print("\r")
            print("Gracias por usar este programa, regresa pronto")

        elif opcion < 1 or opcion > 3:
            print("ERROR, teclea 1, 2 o 3")
            print("\r")

        elif opcion == 1:
            print("\r")
            contarInsectos()

        elif opcion == 2:
            print("\r")
            encontrarMayor()

main()