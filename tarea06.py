# Encoding: Utf-8
# Autor: Viviana Osorio Nieto
# pregunta al usuario cual de las dos funciones quiere hacer (recolectar insector o encotrar el valor mayos)

def recolectarInsectos ():
    insectosR= 0
    insectosF= 30
    dia = 0
    while insectosR < 30:
        insectosR = int(input("cuantos insectos recolectaste hoy?: "))
        insectosF = insectosF - insectosR
        dia = dia +1
        if insectosR <30 :
            print("despues de", dia, "dias, has recolectado", insectosR,"insectos")
            print("te falta recolectar", insectosF,"insectos")
        if insectosR >= 30:
            print("despues de", dia, "dias, has recolectado", insectosR, "insectos")
            print(" te has pasado por",insectosR-30, "insectos")
            print("felicidades!! has llegado a la meta \(^.^)/")
            break

    main()

def encontrarMayor ():  # encuentra el numero mayor de los que el usuario ingresa
    lista = []
    dato = int(input('teclea un numero [-1 pra salir]: '))
    while dato != -1:
        lista.append(dato)
        dato = int(input("teclea un numero [-1 para salir]: "))
    if len(lista) > 0:
        print("mayor:", max(lista))
    else:
        print("No hay datos :( ")
    if dato == -1:
        main()

def main ():
    print("1- Recoletar insectos")
    print("2- Encontrar el mayor")
    print("3- Salir")
    num= int(input("teclea tu opcion: "))
    while num != 3:
        if num == 1:
            recolectarInsectos()
        elif num == 2:
            encontrarMayor()
    if num == 3:
        print("gracias vuelva pronto")


main()