#encoding :UTF-8
#Ernesto Ibhar Guevara Gómez
#A01746121
#Programa que sirve para resolver diferentes ejercicios segun sea la opción del usuario mediante ciclos while.
def recolectarInsectos(): #Funcion que hace el calculo de la recoleccion de los insectos
    insectos=0
    dias=0
    while insectos<30: #Condicion de los insectos para darle resultados al usuario
        cantidadin=int(input("¿Cuantos insectos atrapaste hoy?"))
        dias +=1
        insectos= insectos+cantidadin
        faltantes= 30-insectos
        extra = insectos - 30
        print("Despues de",dias,"dias(s) de recoleccion,llevas:",insectos,"insectos")
        if insectos<=30:
            print("Te hace falta recolectar",faltantes,"insectos")
        else:
            print("Te has pasado",insectos-30,"insectos")
    print("¡Felicidades has llegado a la meta!")
    print("")
    n=""
    return n

def encontrarMayor(): #Funcion que encuentra el numero mayor de una lista que crea el usuario
    lista = []
    dato = int(input("Valor [-1 para salir]: "))
    while dato != -1:
        lista.append(dato)
        dato = int(input("Valor [-1 para salir]: "))
    if len(lista)>0:
        print("El mayor es: ", max(lista))
    else:
        print("No hay valor")
    n=""
    return n


def main(): #Funcion principal
    ejercicio = 1  # Este valor hace que el ciclo de generar el menu sea infinito hasta que él ponga 0 y esto haga que termine.
    while ejercicio == 1:
        # Menú
        print("Tarea 06. Ciclo while ")
        print("Autor: Ernesto Ibhar Guevara Gomez")
        print("")
        print("1. Recolectar insectos")
        print("2. Encontrar el mayor")
        print("3. Salir")
        dato = int(input("Teclea tu opcion: "))
        # Condiciones de menú
        if dato == 3:
            ejercicio = 0
            print("Gracias por usar este programa, regresa pronto.")
        elif dato==1:
            print("Bienvenido al programa que registra los insectos que recolectaste")
            print(recolectarInsectos())
        elif dato==2:
            print(encontrarMayor())
        else:
            print("ERROR,teclea 1,2, o 3")
            print("")

main()
