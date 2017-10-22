#encoding: UTF-8
#Autor: Nazdira Abigail Cerda del Prado A01375428
#Tarea 6: Ciclos while

import sys

#Esta función encuentra el valor del número mayor dentro de una lista dada por el usuario
def encontrarMayor():
    print(("Bienvenido al programa que encuentra el mayor"))
    listadenumeros=[] #Crea lista con los valores dados
    numero = int(input("Teclea un numero [-1 para salir]: ")) #Pregunta al usuario por números
    if numero==-1:
        print("No hay valor mayor")
    else:
        while numero!=-1:
            listadenumeros.append(numero)
            numero=int(input("Teclea un numero [-1 para salir]: "))
        print("El número mayor es: ",max(listadenumeros))

#Esta función le indica al usuario los días de recolección de insectos y si logró llegar a la meta
def recolectarInsectos():
    insectos = 0
    dias = 0
    print("Bienvenido al programa que registra tu avance en la recolección de insectos")

    while insectos < 30:
        numeroinsectos = int(input("¿Cuántos insectos atrapaste hoy? "))
        dias = dias+1
        insectos = insectos + numeroinsectos
        insectosfaltan = 30 - insectos
        insectossobran = insectos - 30

        print ("Después de", dias ,"día(s) de recolección, llevas", insectos, "insectos")

        if insectos < 30:
            print ("Te hace falta recolectar:", insectosfaltan, "insectos")

        else:
            print("Te has pasado con:", insectossobran)
            print("¡Felicidades llegaste a la meta!")


#Esta función funciona como menú para las otras dos anteriores ejecutando la función pedida por el usuario
def main():
    print ("Tarea 6. Ciclos While")
    print ("Autor: Nazdira A. Cerda del Prado A01375428")
    print("--------------------MENU--------------------")
    print("""1)Recolectar insectos 2)Encontrar mayor 3)Salir""")
    selecc=int(input("Teclea tu opción:"))
    while selecc!=3:
        if selecc==1:
            recolectarInsectos()
            print("--------------------MENU--------------------")
            print("""1)Recolectar insectos 2)Encontrar mayor 3)Salir""")
            selecc = int(input("Teclea tu opción:"))
        elif selecc==2:
            encontrarMayor()
            print("--------------------MENU--------------------")
            print("""1)Recolectar insectos 2)Encontrar mayor 3)Salir""")
            selecc = int(input("Teclea tu opción:"))
        elif selecc!=1 or selecc!=2 or selecc!=3:
            print ("ERROR, número no válido")
            print("--------------------MENU--------------------")
            print("""1)Recolectar insectos 2)Encontrar mayor 3)Salir""")
            selecc = int(input("Teclea tu opción:"))
    while selecc==3:
        print("Gracias por usar este programa, regresa pronto")
        break
        sys.exit

main()