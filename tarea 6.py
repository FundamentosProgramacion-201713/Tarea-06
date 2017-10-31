# encoding UTF-8
# Autor: Andrea Montero Rivas, A01374496
# Descripción: Tarea 6, ciclos while

def registroInsectos():
    print("Bienvenido al programa que registra los insectos que recolectas")
    colecta = 0
    dia = 0
    while  colecta < 30:
        dia += 1
        colecta += int(input("¿Cuántos insectos atrapaste hoy?"))
        print("Después de %d día(s) de recolección, llevas %d insectos" %(dia, colecta))
        if colecta < 30:
            print("Te hace falta recolectar %d insectos" %(30-colecta))
        elif colecta == 30:
            print("¡Felicidades, has llegado a la meta!")
            seleccionMenu()
        else:
            print("Te has pasado con %d insectos" %(colecta - 30))
            print("¡Felicidades, has llegado a la meta!")
            seleccionMenu()

def encontrarMayor():
    print("Bienvenido al programa que encuentra el mayor de los números")
    num = []
    a = 0
    while a != -1:
        a = int(input("Teclea un número [-1 para salir]:"))
        num.append(a)
        x = max(num)
    if x ==-1:
        print("No hay valor mayor")
    else:
        print("El mayor es:",x)
    seleccionMenu()

def seleccionMenu():
    print('''MENU
    1. Recolectar insectos
    2. Encontrar el mayor
    3. Salir''')
    seleccion = 0
    while seleccion != 3:
        seleccion = int(input("Teclea tu opción"))
        if seleccion == 1:
            registroInsectos()
        elif seleccion == 2:
             encontrarMayor()
        else:
             quit()

def main():
    seleccionMenu()
main()