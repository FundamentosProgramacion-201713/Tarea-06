#encode: UTF-8
# Autor: David Ramírez Ríos, A01338802
# Descripción: Dos funciones con ciclos While y un menú en la función main para elegir

def contarInsectos():
    nInsectos =  0
    dias = 0
    print("Bienvenido al programa que registra los insectos que recolectas ")
    while nInsectos < 30:
        nInsectos += int(input("¿Cuántos insectos atrapaste hoy? "))
        dias += 1
        print("Después de %d día(s) de recolección, llevas %d insectos " % (dias, nInsectos))
        diferencia = 30 - nInsectos
        if diferencia >= 0:
            print("Te hace falta recolectar %d insectos" % (diferencia))
        else:
            print("Te has pasado con %d insectos" % (diferencia*-1))
    print("¡Felicidades, has llegado a la meta!")

def encontrarMayor():
    print("Bienvenido al programa que encuentra el mayor ")
    conjunto = []
    numero = int(input("Teclea un número [-1 para salir] "))

    while numero > -1:
        conjunto.append(numero)
        numero = int(input("Teclea un número [-1 para salir] "))
    if len(conjunto) != 0:
        mayor = max(conjunto)
        print("El mayor es ", mayor)
    else:
        print("No hay mayor ")

def main():
    menu = """
    Tarea 06. Ciclos While
    Autor: David Ramírez Ríos
    
    1. Recolectar insectos
    2. Encontrar el mayor
    3. Salir
    """
    opcion = int(input(menu + "Teclea tu opción: "))
    while opcion!= 3:
        if opcion == 1:
            contarInsectos()
        elif opcion == 2:
            encontrarMayor()
        else:
            print("Error, tecela 1, 2 o 3 ")
        opcion = int(input(menu + "Teclea tu opción: "))
    print("Gracias por usar este programa ")

main()