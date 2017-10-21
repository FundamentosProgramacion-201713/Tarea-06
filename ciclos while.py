#encode: UTF-8
#Autor: Leonardo Castillejos Vite
#Descripción: Programa que dice cuantos insectos faltan por atrapar y el mayor número de un conjunto


def main():
    opcion = 0
    while opcion != 3:
        print("1. Recolectar insectos", "\n", "2. Encontrar el mayor ", "\n", "3. Salir", sep="")
        opcion = int(input("Teclea tu opción: "))
        if opcion == 1:
            recolectarInsectos()
        elif opcion == 2:
            encontrarMayor()


#La función pregunta cuantos insectos se atraparon y dice el número de días que han pasado y la cantidad de insectos
#que faltan para llegar a la meta de insectos y dice si se atraparon extra.
def recolectarInsectos():
    insectos = 0
    atrapados = 0
    dias = 0
    meta = 30
    faltantes = 30
    while insectos < meta:
        print("Bienvenido al programa que registra los insectos que recolectas")
        atrapados = int(input("¿Cuántos insectos atrapaste hoy? "))
        insectos += atrapados
        dias += 1
        faltantes -= atrapados
        print("Después de %d días(s) de recolección llevas %d insectos" %(dias, insectos))
        if insectos > 30:
            sobrantes = insectos - 30
            print("Te has pasado con %d insectos" % (sobrantes))
        else:
            print("Te hace falta recolectar %d insectos" %(faltantes))
    print("¡Felicidades, has llegado a la meta!")


#Es un programa al que el usuario le da números hasta que el usuario escribe -1 y el programa da el mayor de los números
#introducidos
def encontrarMayor():
    n = 0
    lista = []
    print("Bienvenido al programa que encuentra el mayor")
    while n != -1:
        n = int(input("Teclea un número [-1 para salir]: "))
        lista.append(n)
    if max(lista) == -1:
        print("No hay valor mayor")
    else:
        print("El mayor es: ", max(lista))



main()