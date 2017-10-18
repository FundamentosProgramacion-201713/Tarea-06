#encoding: UTF-8
#Autor: Javier Martínez Hernández
#Descripcion: se harán ciclos con while, utilizando contadores

def colectaInsectos():
    print("Bienvenido al programa que registra los insectos que recolectas")
    valido=True
    insectos=int(input("¿Cuantos insectos capuraste hoy? "))
    dias=0
    while valido:
        dias+=1
        print("Despues de %d día(s) de recolecció, llevas %d insectos"%(dias,insectos))
        if insectos >= 30:
            print("Te has pasado por",insectos-30,"insectos")
            print("¡Felicidades, has llegado a la meta!")
            valido=False
        elif insectos==30:
            print("Te hace falta recolectar",30-insectos,"insectos")
            print("¡Felicidades, has llegado a la meta!")
            valido=False
        else:
            print("Te hacen falta",30-insectos,"insectos")
            insectos += int(input("¿Cuantos insectos capuraste hoy? "))
    main()
def encuentraMayor():
    print("Bienvenido al programa que encuentra el numero mayor")
    listaNum=[]
    valorDado=int(input("Teclea un número [-1 para salir]: "))
    if valorDado!=-1:
        while valorDado!=-1:
            listaNum.append(valorDado)
            valorDado = int(input("Teclea un número [-1 para salir]: "))
        print("El numero mayor es: ",max(listaNum))
        main()
    else:
        print("No hay valor mayor")
        main()
def main():
    print('''Tarea.06 Ciclos While
Autor: Javier Martínez
1. Recolectar Insectos
2. Encontrar el Mayor
3. Salir''')
    opcionUsuario=int(input("Teclea tu opcion: "))
    if opcionUsuario==1:
        colectaInsectos()
    elif opcionUsuario==2:
        encuentraMayor()
    elif opcionUsuario==3:
        print("Gracias por usar este programa, regresa pronto")
    else:
        print("ERROR, teclea 1,2 o 3")
        main()
main()