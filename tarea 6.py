# encoding: UTF-8
# Autor: Eduardo Gallegos Solís
# Programa que calcula el número de insectos que atrapas y el mayor número que ingreses en el programa

def calcularInsectos():
    listaInsectos=[]
    meta = False
    while meta == False:
        insectos = int(input("¿Cuántos insectos atrapaste hoy?"))
        listaInsectos.append(insectos)
        dias = len(listaInsectos)
        insectosTotales = sum(listaInsectos)
        sumaTotal = 30 - sum(listaInsectos)
        if sum(listaInsectos)<30:
            print('Después de',dias,' día(s) de recolección, llevas',insectosTotales,'insectos')
            print('Te hace falta recolectar', sumaTotal, 'insectos')
            meta = False
        elif sum(listaInsectos)== 30:
            print('Después de', dias, ' día(s) de recolección, llevas', insectosTotales, 'insectos')
            print('Te hace falta recolectar', sumaTotal, 'insectos')
            print("!Felicidades, has llegado a la meta¡")
            meta = True
        elif sum(listaInsectos)>30:
            excesoInsectos = sum(listaInsectos) - 30
            print('Después de', dias, ' día(s) de recolección, llevas', insectosTotales, 'insectos')
            print("Te has pasado con %.d insectos" %excesoInsectos)
            print("!Felicidades, has llegado a la meta¡")
            meta = True

def calcularMayor():
    lista = []
    n = int(input("Teclea el número [-1 para salir]"))
    while n != -1:
        lista.append(n)
        n = int(input("Teclea el número [-1 para salir]"))
        if len(lista) > 0:
            resultado = max(lista)
        else:
            print("No hay resultados")
    return resultado

def main():
    opcion = -1
    while opcion != 3:
        print('''
Tarea 06. Ciclos While
Autor: Eduardo Gallegos Solís

1. Recolestar insectos
2. Encontrar el mayor
3. Salir''')
        opcion = int(input("Teclea tu opción: "))
        if opcion == 1:
            print("Bienvenido al programa que registra los insectos que recolectas")
            print(calcularInsectos())
        elif opcion == 2:
            print("Bienvenido al programa que encuentra el mayor")
            print("El mayor es:", calcularMayor())
        elif opcion == 3:
            print("Gracias por usar este programa, regrese pronto.")
        elif opcion<=0:
            print("ERROR, teclea 1, 2 o 3")
        elif  opcion>=4:
            print("ERROR, teclea 1, 2 o 3")


main()