#encoding: UTF-8
#Autor: Luis Fernando Figueroa Rendon, A01746139
#Realizar problemas utilizando el ciclo "while"


#Esta funcion analiza la cantidad de insectos que se han recolectado en un cierto periodo de tiempo.
def recolectarInsectos():
    insectos=0
    dias=0
    while insectos < 30:
        recolectado= int(input("¿Cuantos insectos atrapaste hoy? "))
        if recolectado < 0:
            print("Teclea numeros positivos.")
        else:
            dias += 1
            insectos += recolectado
            faltantes= 30 - insectos
            print("Despues de ", dias, "dia(s) de recoleccion, llevas ", insectos, "insectos.")
            if faltantes>=0:
                print("Te hace falta recolectar ", faltantes, "insectos.")
            elif faltantes<0:
                print("Te has pasado con ", insectos-30, "insectos.")
    print("Felicidades has llegado a la meta.")
    n= ""
    return n

#Funcion la cual enlista numeros y dice cual es el mayor.
def encontrarMayor():
    lista = []
    numero = int(input("Valor [-1 para salir]: "))
    while numero != -1:
        lista.append(numero)
        numero = int(input("Valor [-1 para salir]: "))
    if len(lista) > 0:
        print("El mayor es: ", max(lista))
    else:
        print("No hay valor.")
    n= ""
    return n

#Funcion principal del programa en donde se imprimen las funciones y se encuentra el menu.
def main():
    ejercicio = 1
    #Inicia el menu.
    while ejercicio == 1:
        print("Tarea 06. Ciclos while.")
        print("Autor: Luis Fernando Figueroa Rendon.")
        print("")
        print("1. Recolectar insectos.")
        print("2. Encontrar el mayor.")
        print("3. Salir")
        usuario= int(input("Teclea tu opcion: "))
        print("")
        #Si se teclea 1 se realizara la funcion de recolectar insectos.
        if usuario==1:
            print("Bienvenido al programa que registra los insectos que recolectas ")
            print(recolectarInsectos())

        #Si se teclea 2 se realizara la funcion de encontrar el mayor.
        elif usuario==2:
            print("Bienvenido al programa que encuentra al mayor.")
            print(encontrarMayor())

        #Si se teclea 3 se saldra del programa.
        elif usuario==3:
            ejercicio=0
            print("Gracias por usar este programa, regrese pronto!!!")

        #Si se teclea algun valor diferente a 1, 2 o 3 se pedira ingresar alguno de esos 3 numeros.
        else:
            print("ERROR, teclea 1, 2 o 3 " )
            print("")


main()