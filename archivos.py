#encoding: utf-8
#coded by: jordan

def bugCollecter():
    count = 0
    acum = 1
    while count < 30:
        bugs = int(input("¿Cuántos insectos atrapaste hoy? "))
        count += bugs
        print("Después de %d día(s) de recolección, llevas %d insectos" % (acum, count))
        acum += 1
        if count < 30:
            need = 30 - count
            print("Te hacen falta %d insectos" % need)
    if count > 29:
        res = count - 30
        if res > 0:
            print("Te has pasado con %d insectos" % res)
        else:
            print("No te has pasado de insectos")
    print("¡Felicidades, has llegado a la meta!")

def highestNFinder():
    numbers = []
    n = int(input("Teclea un número [-1 para salir]: "))
    while n != -1:
        if n < 0:
            n = int(input("No se aceptan números negativos. \n Teclea un número [-1 para salir]: "))
        else:
            numbers.append(n)
            n = int(input("Teclea un número [-1 para salir]: "))
    if not numbers:
        print("No hay valor mayor")
    else:
        print("El número mayor es : " + str(max(numbers)))

def main():
    menu = "\n---------------------------------\nTarea 06. Ciclos While\nAutor: Jordan González Bustamante\n1. Recolectar insectos\n2. Encontrar el mayor\n3. Salir\n---------------------------------"
    print(menu)
    opt = int(input("Teclea tu opción: "))
    while True:
        if opt == 1:
            print("Bienvenido al programa que registra los insectos que recolectas")
            bugCollecter()
            print(menu)
            opt = int(input("Teclea tu opción: "))
        elif opt == 2:
            print("Bienvenido al programa que encuentra el mayor")
            highestNFinder()
            print(menu)
            opt = int(input("Teclea tu opción: "))
        elif opt == 3:
            print("Gracias por usar este programa, regresa pronto.")
            break
        else:
            print("ERROR, teclea 1, 2 o 3")
            print(menu)
            opt = int(input("Teclea tu opción : "))
            while opt < 0 and opt > 4:
                opt = int(input("Teclea tu opción : "))

main()