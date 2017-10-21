#Encoding: UTF-8
#Autor: Roberto Téllez Perezyera
"""
Este programa permite al usuario contabilizar los insectos que recolecta un niño cada día o encontrar el mayor de un
conjunto de enteros positivos que éste puede ingresar.
Se puede acceder a cualquiera de estos dos programas mediante un menú principal.
"""

def contabilizarInsectos():
    #Contabiliza e informa sobre los insectos capturados de forma contínua hasta que se alcanza la meta de 30 insectos.
    contador = 0
    goal = 30
    userAns = 0
    while userAns < 30:
        print("Bienvenido al programa que registra los insectos que recolectas.")
        userAns += int(input("¿Cuántos insectos atrapaste hoy? "))
        contador += 1
        print("Después de %2d día(s) de recolección, llevas %2d insectos." % (contador, userAns))

        if userAns < goal:
            print("Te hace falta recolectar %2d insectos\n" % ((goal - userAns)))

        elif userAns > goal:
            print("Te has pasado con %2d insectos" % (userAns - goal))

    print("¡Felicidades, has llegado a la meta!\n")


def encontrarMayor():
    #Encuentra el valor mayor de los números introducidos por el usuario
    lista = []
    print("Bienvenido al programa que encuentra el mayor.")
    userAns = int(input("Teclea un número [-1 para salir]: "))
    lista.append(userAns)
    while userAns != -1:        #Si el usuario teclea -1 inicialmente, terminó sin insertar datos.
        userAns = int(input("Teclea un número [-1 para salir]: "))
        lista.append(userAns)
    if len(lista) == 1:
        print("No hay valor mayor.\n")
    elif max(lista) == -1:      #Discriminamos a -1 porque es la instrucción para terminar.
        lista.remove(-1)        #Seguiremos dando el valor mayor correcto, incluso si todas las entradas son negativas.
        print("El mayor es: ", max(lista), "\n")
    else:
        print("El mayor es: %d\n" % (max(lista)))


def main():
    #Es el menú principal de la tarea

    termina = False
    while not termina:

        print("""Tarea 06. Ciclos while
        Autor: Roberto Téllez Perezyera
        
        1. Recolectar insectos
        2. Encontrar el mayor
        3. Salir
        """)

        userChoice = int(input("Teclea tu opción: "))

        if userChoice == 1:
            contabilizarInsectos()
        elif userChoice == 2:
            encontrarMayor()
        elif userChoice == 3:
            print("Gracias por usar este programa, regresa pronto.")
            termina = True
        else:
            print("\nERROR, teclea 1, 2 o 3\n")


main()
