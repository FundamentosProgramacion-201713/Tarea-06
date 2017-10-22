#encoding: UTF-8
#Autor: Maria Fernanda Torres Velazquez A01746537
#Descripcion: El siguiente programa, muestra un menu al usuario que le permite escoger 2 opciones, posteriormente
#mediante un ciclo while, se ejcutaran cuantas veces el usuario lo desee

def registrarColeccion(): #Registra el numero de insectos y muestra cuantos lleva recolectados, cuantos le faltan y cuantos le sobran

    print ("BIENVENIDO A TU REGISTRO DE INSECTOS")
    print ("------------------------------------")
    insectos = 0
    dia= 0

    while not insectos >=30:
        recolectados=(int(input("¿Cuantos insectos recolectaste hoy? ")))
        insectos = insectos + recolectados
        dia= dia+1
        restantes= 30 - insectos
        excedente= insectos-30

        print ("Despues de: %d dias, llevas %d insectos recolectados" %(dia,insectos))

        if restantes >0 and restantes<30:
            print ("Te faltann: %d insectos" %restantes)
        elif restantes == 0:
            print ("Muchas felicidades has llegado a la meta, recolectaste 30 insectos")
        elif excedente > 0:
            print ("Muchas felicidades has llegado a la meta, recolectaste: %d insectos" %insectos)
            print ("Recolectaste %d insectos mas de tu meta" %excedente)

def encontrarMayor(): #Registra numeros y muestra el mayor
    print("BIENVENIDO AL PROGRAMA QUE ENCUENTRA EL MAYOR")
    print("---------------------------------------------")

    lista = []
    numero=(int(input("Introduce un numero [-1 para salir]: ")))
    if numero==-1:
        print ("HASTA LUEGO")
    else:
        while numero != -1:
            lista.append(numero)
            numero = (int(input("Introduce un numero [-1 para salir]: ")))

    if len(lista) > 0:
        print("-----------------------------------------")
        print("EL NUMERO MAYOR ES: ", max(lista))

    elif len(lista) == 0:
        print("LISTA VACIA, NO HAY VALOR MAXIMO")


def main():
    print ("BIENVENIDO, A CONTINUACION TE MOSTRAMOS EL MENU DE OPCIONES:")
    print ("------------------------------------------------------------")
    print ("                1. Recolectar insectos                      ")
    print ("                2. Encontrar  el mayor                      ")
    print ("                3.      S A L I R                           ")
    opcion=(int(input("  POR FAVOR ELIGE UNA OPCION: ")))
    print("------------------------------------------------------------")

    while opcion != 3:
        if opcion == 1:
            print("------------------------------------------------------------")
            registrarColeccion()
            print("------------------------------------------------------------")

        elif opcion == 2:
            print("------------------------------------------------------------")
            encontrarMayor()
            print("------------------------------------------------------------")

        else:
            print("------------------------------------------------------------")
            print ("OPCION INVALIDA, SOLO PUEDES INTRODUCIR NUMEROS ENTRE 1 Y 3")
            print("------------------------------------------------------------")

        print ("------------------------------------------------------------")
        print ("                1. Recolectar insectos")
        print ("                2. Encontrar  el mayor")
        print ("                3.      S A L I R     ")
        opcion=(int(input("  POR FAVOR ELIGE UNA OPCION: ")))
        print("------------------------------------------------------------")


main()






