# encoding : utf-8
# autor: Iván Alejandro Dumas Martínez

def bugCollection():
    print("\nBienvenido al programa que registra los insectos que recolectas")
    days = 0
    remaining = 30
    bugs = 0
    while bugs < 30:
        bugs += int(input("¿Cuantos insectos atrapaste hoy? "))
        days += 1
        remaining = 30 - bugs
        print("Después de %d día(s) de recolección, llevas %d insectos" % (days, bugs))
        if bugs <= 30:
            print("Te hace falta recolectar %d insectos" % remaining)
        else:
            print("Te has pasado con %d insectos" % (-remaining))

    print("¡Felicidades, has llegado a la meta!\n\n")

def findingBigestNum():
    numList =[]
    num = int(input("""
Bienvenido al programa que encuentra el mayor
Teclea un número [-1 para salir]: """))
    mayor = "No hay mayor"
    while num != -1:
        num = int(input("Teclea un número [-1 para salir]: "))
        numList.append(num)
    if numList:
        if -1 in numList:
            numList.remove(-1)
        mayor = max(numList)
    else:
        print("ERROR: No hay números por procesar")
    return mayor

def main():
    option = 0
    while option != 3:
        option = int(input("""Tarea 06. Ciclos while
Autor: Iván Alejandro Dumas Martínez

1. Recolectar insectos 
2. Encontrar el mayor 
3. Salir
Teclea tu opción: """))
        if option == 1:
            bugCollection()
        elif option == 2:
            print("El mayor es: ",findingBigestNum(),"\n\n")
        elif option < 1 or option > 2 and option != 3:
            print("ERROR, teclea 1, 2 o 3\n\n")

    print("\nGracias por usar este programa, regresa pronto.")

if __name__ == '__main__':
    main()