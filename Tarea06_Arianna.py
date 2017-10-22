# encoding: UTF-8
# Autor: Arianna Sinai Soriano Vega
# Tarea 06. Ciclos While

def insectosRecolectados():
    print("Bienvenido al programa que registra los insectos que recolectas")
    insect=0
    anterior = 0
    dia = 1
    resta=0
    while insect <30:
        insect = int(input("¿Cuántos insectos atrapaste hoy?"))
        total = insect + anterior
        anterior = total
        print("Depués de ", dia, "día(s) de recolección, llevas ", total,"insectos.")
        dia=dia+1

        if total<30:
            resta = 30 - total
            print("Te hace falta recolectar ", resta, "insectos")
        elif total==30:
            resta = 30 - total
            print("Te hace falta recolectar ", resta,"insectos")
            print("¡Felicidades, has llegado a la meta!")
            break
        elif total>30:
            resta= total-30
            print("Te has pasado por ", resta,"insectos")
            print("¡Felicidades, has llegado a la meta!")

            break

def enteroMayor():
    print("Bienvenido al programa que encuentra el mayor")
    num = int(input("Teclea un número [-1 para salir]:"))
    lista=[]
    if num==-1:
        print("No hay valor mayor")
    else:
        while num > -1:
            num = int(input("Teclea un número [-1 para salir]:"))
            lista.append(num)
            if num == -1:
                print("El mayor es:", max(lista))


            
def menu():
    print("Tarea 06. Ciclos while")
    print("Autor: Arianna Sinai Soriano Vega")
    print("")
    print("1. Recolectar insectos")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opcion: "))
    if opcion==3:
        print("")
        print("Gracias por usar este programa, regresa pronto.")
        exit()
    while opcion != 3:
        if opcion == 1:
            print("")
            insectosRecolectados()
            print("")
            menu()
        elif opcion == 2:
            print("")
            enteroMayor()
            print("")
            menu()
        elif opcion == 3:
            print("Gracias por usar este programa, regresa pronto.")
            break
        else:
            print("ERROR, teclea 1,2 o 3")
            menu()

def main():
    print("Tarea 06. Ciclos while")
    print("Autor: Arianna Sinai Soriano Vega")
    print("")
    print("1. Recolectar insectos")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion=int(input("Teclea tu opcion: "))
    if opcion==3:
        print("")
        print("Gracias por usar este programa, regresa pronto.")
        exit()
    while opcion!=3:
        if opcion==1:
            print("")
            insectosRecolectados()
            print("")
            menu()
        elif opcion==2:
            print("")
            enteroMayor()
            print("")
            menu()

        elif opcion>3:
            print("ERROR, teclea 1,2 o 3")
            menu()
            print("")




main()