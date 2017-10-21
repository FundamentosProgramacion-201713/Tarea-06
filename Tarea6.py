# encoding UTF-8
# Jaime Orlando López Ramos, A01374696

# Programa que pueda ayudar a un niño a llevar el conteo de insectos recolectados o encontrar el número mayor dentro de
# una serie de números

def calcularInsectos():
    print("Bienvenido al programa que te ayuda a llevar el conteo de insectos recolectados")
    insectos = 0
    counterInsectos = 0
    dias = 0
    while counterInsectos < 30:
        insectosDia = int(input("¿Cuántos insecto recolectaste hoy?: "))
        counterInsectos = counterInsectos + insectosDia
        dias = dias +1
        print("has recolectado", counterInsectos, "en", dias, "día(s)")
        if counterInsectos <= 30:
            print("Te hace falta recolectar", 30-counterInsectos, "para llegar a la meta" )
        else:
            print ("Te hacen falta 0 insectos y te has pasado por", counterInsectos-30, "Insectos")

    print("Felicidades, lo lograste")


def calcularMayor():
    lista = []
    a = int(input("Ingrese un valor (-1 para salir): "))
    while (a > -1) and (a!= 0):
        if a != -1:
            lista. append(a)
            a = int(input("Ingrese un valor (-1 para salir): "))
    if (a == -1 and (lista != [])):
        print("El mayor es:", max(lista))
        print("fin del programa")
    elif a == -1 and lista == []:
        print("lista vacía")
    elif a < -1:
        print("Este programa no trabaja con enteros negativos")

def main():
    a = int(input("""Qué desea hacer?
    1.- Recolectar Insectos
    2.- Encontrar mayor
    3.- Salir
    Teclee el número deseado: """))
    while a != 3:
        if a == 1:
            calcularInsectos()
        elif a == 2:
            calcularMayor()
        else:
            print("Por favor, teclee 1, 2 ó 3")
        a = int(input("""Qué desea hacer?
        1.- Recolectar Insectos
        2.- Encontrar mayor
        3.- Salir
        Teclee el número deseado: """))

    print("Programa Terminado")


main()

