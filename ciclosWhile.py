#encoding: UTF-8
#Autor: Luis Alfonso Alcántara López Ortega

def calcularInsectos():
    #Función que calcula la cantidad de insectos que se ha recolectado hasta que tenga 30 o más
    contador = 0
    insectosRecolectados = 0
    print("""\nBienvenido que registra los insectos
que recolectas""")
    while insectosRecolectados < 30:
        insectosRecolectados += int(input("¿Cuántos insectos atrapaste hoy? "))
        contador += 1
        insectosFaltantes = 30 - insectosRecolectados

        print("Después de", contador, "día(s) de recolección, llevas", insectosRecolectados)
        print("insectos.")
        if insectosFaltantes < 0:
            print("Te has pasado con", insectosFaltantes * -1, "insectos")
        else:
            print("Te hace falta recolectar", insectosFaltantes, "insectos")
    print("¡Felicidades, has llegado a la meta!\n\n")

def calcularMayor():
    #Función que calcula el número mayor de un conjunto de enteros positivos dados por el usuario
    print("""\nBienvenido al programa que encuentra el mayor""")

    numero = 0
    contador = 0
    mayor = -1
    while numero !=-1:
        numero = int(input("Teclea un número [-1 para salir]: "))
        if numero != 0:
            contador +=1
        if numero > mayor and numero > 0:
            mayor = numero
    if contador == 0 or mayor == -1:
        print("No hay valor mayor\n\n")
    else:
        print("El mayor es:", mayor,"\n\n")

def main():
    #Función que despliega el menú principal con opciones para el usuario
    termina = False

    while not termina:
        print("""Tarea 06. Ciclos while
Autor: Luis Alfonso Alcántara

1. Recolectar insectos
2. Encontrar el mayor
3. Salir""")

        opcion = int(input("Teclear tu opción: "))
        if opcion == 1:
            calcularInsectos()
        elif opcion == 2:
            calcularMayor()
        elif opcion == 3:
            termina = True
        else:
            print("ERROR, teclea 1, 2 o 3\n\n")
    print("\nGracias por usar este programa, regresa pronto.")
main()