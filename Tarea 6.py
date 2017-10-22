# encoding: UTF-8
# Autor: Ángel Guillermo Ortiz González A01745998
# Menú que da opción a elegir dos programas: contador de insectos y mayor en una lista

def registrarInsectos():
    print(" ")
    print("Bienvenido al programa que registra los insectos que recolectas")
    print(" ")
    insectos = int(input("¿Cuántos insectos atrapaste hoy? "))
    dia = 0 # contador días
    recolectados = 0 # contador insectos

    terminar = False

    while not terminar:
        if insectos < 0: # para no aceptar valores negativos
            print("ERROR. Inserte un número válido.")
            print(" ")
            insectos = int(input("¿Cuántos insectos atrapaste hoy? "))
        dia += 1
        recolectados += insectos
        diferencia = 30 - recolectados
        if recolectados < 30 and recolectados >= 0: # para cuando faltan insectos para los 30.
            print("Después de %d día(s) de recolección, llevas %d insectos." % (dia,recolectados))
            print("Te hacen falta recolectar %d insectos." % (diferencia))
            print(" ")
            insectos = int(input("¿Cuántos insectos atrapaste hoy? "))

        else: # cuando pasan los 30 insectos
            print("Después de %d día(s) de recolección, llevas %d insectos." % (dia,recolectados))
            print("Te has pasado con", -diferencia, "insectos")
            print("¡Felicidades, has llegado a la meta!")
            terminar = True

def encontrarMayor():
    print(" ")
    print("Bienvenido al programa que encuentra el mayor")
    lista = []
    numero = int(input("Teclea un número [-1 para salir]: "))
    while numero != -1: # mientras no sea -1
        lista.append(numero) # agregar a la lista
        numero = int(input("Teclea un número [-1 para salir]: ")) # pedir más valores
    if len(lista) > 0: # cuando se tiene un número o más
        print(" ")
        print("El mayor es:",max(lista))
    else: # cuando no se tienen números
        print(" ")
        print("Por favor introduzca datos, su lista está vacía.")


def main():
    print("Tarea 6. Ciclos while")
    print("Autor: Ángel Guillermo Ortiz González")
    print(" ")
    print("1. Recolectar insectos")
    print("2. Encontrar el mayor")
    print("3. Salir")
    print(" ")
    opcion = int(input("Teclea tu opción: "))

    salir = False
    while not salir:
        if opcion == 1:
            registrarInsectos()

        elif opcion == 2:
            encontrarMayor()

        elif opcion == 3:
            print(" ")
            print("Gracias por usar este programa. ¡Hasta pronto!")
            salir = True
            quit()

        else:
            print("ERROR, teclea 1, 2, 3")
        print(" ")
        opcion = int(input("Teclea tu opción: "))

main()