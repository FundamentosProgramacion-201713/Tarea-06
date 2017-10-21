#encoding:UTF-8
#Autor: José Antonio Gómez
#El usuario escribe la opción que quiere ejecutar en el menú, ya sea contar insectos, encontrar el mayor de una lista de números o salir.

#cuenta insectos
def contarInsectos():
    cInsectos=0
    cDias=0
    while cInsectos <= 29:
        insectos = int(input("Teclea el número de insectos recolectados hoy: "))
        cInsectos += insectos
        cDias += 1
        print("\nDespués de %d día(s), llevas %d insectos." % (cDias, cInsectos))

    if cInsectos == 30:
        print("Te hace falta recolectar 0 insectos.")
        print("\n¡Felicidades, has llegado a la meta!\n")

    else:
        extra = cInsectos - 30
        print("Te has pasado por %d insectos." % extra)
        print("\n¡Felicidades, has llegado a la meta!\n")

#calcula el mayor con la lista que recibe como parámetro
def encontrarMayor(valores):
    return max(valores)


def main():

    menu=True
    print("Tarea 6")
    print("-------")
    print("Bienvendio al programa\n")
    print("""1. Recolectar insectos
2. Encontrar el mayor
3. Salir""")
    seleccion=int(input("Teclea opción: "))

    #menu
    while menu==True:
        #Selección no se encuentra
        if seleccion == 0 or seleccion >= 4:
            print("\nLa opción no se encuentra en el menú. Intenta nuevamente.\n")
            print("""1. Recolectar insectos
2. Encontrar el mayor
3. Salir""")
            seleccion = int(input("Teclea opción: "))

        #Selección negativa
        if seleccion <= -1:
            print("\nError. Escribe números positivos. Intenta nuevamente.\n")
            print("""1. Recolectar insectos
2. Encontrar el mayor
3. Salir""")
            seleccion = int(input("Teclea opción: "))

        #selección contar insectos
        if seleccion==1:
            print("\nSeleccionaste 'Contar insectos'. !La meta son 30 insectos!¡Buena suerte!\n")
            contarInsectos()
            print("""1. Recolectar insectos
2. Encontrar el mayor
3. Salir""")
            seleccion = int(input("Teclea opción: "))

        #selección encontrar el mayor
        if seleccion==2:
            print("\nSeleccionaste 'Encontrar el mayor'\n")
            valor=int(input("Teclea un número[-1 para salir]: "))


            if valor != -1:
                listaValores=[valor]
                while valor!=-1:
                    valor = int(input("Teclea un número[-1 para salir]: "))
                    if valor != -1:
                        listaValores.append(valor)
                    else:
                        print("\nEl mayor es:",(encontrarMayor(listaValores)))

            if valor==-1:
                print("""\n1. Recolectar insectos
2. Encontrar el mayor
3. Salir""")
            seleccion = int(input("Teclea opción: "))

        #selección salir
        if seleccion==3:
            menu=False
            print("\nGracias por tu visita. ¡Vuelve pronto!")
main()