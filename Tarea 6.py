# encoding:UTF-8
# Autor: Carlos Pano Hernández
    #Tarea 06. Ciclos while


# Descripción: Este progrma resuelve múltiples ejercicios como un contador de insectos y contador del mayor número en una lista.

def contarInsectos():
    print("")
    print("Bienvenido al programa que registra los insectos que recolectas")
    print("")

    insectos=0
    dias=0
    restantes=30

    while insectos<=30:
        cantidad=int(input("¿Cuántos insectos atrapaste hoy?"))
        dias=dias+1
        insectos=insectos+cantidad

        if insectos>=30:
            print("Después de", dias, "día(s) de recolección, llevas:", insectos, "insectos.")
            print("Te has pasado con", insectos-30, "insectos.")
            print("")
            print("¡Felicidades, has llegado a la meta!")
            print("")
            break

        print("Después de",dias,"día(s) de recolección, llevas:",insectos,"insectos.")
        print("")
        print("Te hace falta recolectar",restantes-insectos,"insectos")

def escogerMayor():
    print("")
    print("Bienvenido al programa que encuentra el mayor")
    while


def main():
    seleccion=0

    while seleccion>=0:
        print("""Tarea 06. Ciclos While
Autor: Carlos Pano Hernández
        
        1. Recolectar insectos
        2. Encontrar el mayor
        3. Salir
        """)

        seleccion=int(input("Teclea tu opción:"))

        if seleccion==1:
            contarInsectos()

        elif seleccion==2:
            escogerMayor()

        elif seleccion==3:
            print("")
            print("Gracias por usar este programa, regresa pronto.")
            break
        else:
            print("")
            print("ERROR, teclea 1,2,3")
            print("")

main()

