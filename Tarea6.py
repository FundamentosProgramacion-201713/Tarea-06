#encoding: UTF-8
#Autor: Irving Fuentes Aguilera
#Descripción: Programa que hace un conteo de insectos recolectados

def contarInsectos():
    dias=0
    insectos=0
    total=0
    print("Bienvenido al programa que registra los insectos que recolectas")


    while insectos<30:
        insectos = int(input("¿Cuantos insectos recolectaste hoy? "))
        dias += 1
        total= insectos + total
        restante = 30 - total
        print("Después de %d día(s) de recolección llevas %d insectos" % (dias,insectos))
        if restante<0:
            restante=0
        print("Te hace falta recolectar %d insectos" % restante )

        if insectos == 30:
            restante= 0
            print("¡Felicidades, has llegado a la meta!")

        elif insectos > 30:
            restante=0
            print("Te has pasado por %d insectos" % (insectos - 30))
            print("¡Felicidades, has llegado a la meta!")


def calcularMayor():
    print("Bienvenido al programa que calcula el número mayor")
    lista= []
    dato=int(input("Teclea el número (-1 para salir): "))
    while dato != -1:
        lista.append(dato)
        dato=int(input("Teclea el número (-1 para salir): "))

    if len(lista)>0:
        print("El mayor es: ", max(lista))
    else:
        print("No hay mayor")


def main():
    print("1.- Recolectar insectos \n"
          "2:- Calcular el mayor \n"
          "3.- Salir")
    opcion= 0
    while opcion !=3:
        opcion = int(input("Introducir la opción que quieras ver: "))
        if opcion==1:
            contarInsectos()
        elif opcion==2:
            calcularMayor()
        else:
            print("Teclea una opción válida")
    if opcion==3:
        print("Gracias por usar este programa, vuelva pronto")

main()

