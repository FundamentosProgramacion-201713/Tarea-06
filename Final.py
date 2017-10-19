# ecnoding: UTF-8
# Autor: LuisMiguel Baqueiro
# Matricula: 1745997
# Funciones para recolectar los insectos y saber el mayor número
def calcularInsectos():
    print("")
    print("Bienvenido al programa que registra los insectos que recolectas")
    insectos = 0
    dias = 0
    while insectos < 30:
        insectos += int(input("¿Cuántos insectos atrapaste hoy? "))
        dias += 1
        print("Después de %s día(s) denrecolección, llevas %s insectos" % (dias, insectos))
        falta = 30 - insectos
        if insectos <= 30:
            print("Te hace falta recolectar %s insectos" % falta)
        else:
            print("Te has pasado con %s insectos" % (falta + (falta * -2)))
        if insectos >= 30:
            print("¡Felicidades, has llegado a la meta!")
            print("")


def encuentraElMayor():
    print("")
    print("Bienvenido al programa que encuentra el mayor")
    lista = []
    dato = int(input("Valor [-1 para salir]: "))
    while dato != -1:
        lista.append(dato)
        dato = int(input("Valor [-1 para salir]: "))
    if dato == -1 and len(lista) == 0:
        print("No hay valor mayor")
        print("")
    else:
        print("El mayor es: ", max(lista))


def main():
    numero = 0
    while numero != 3:
        print("""Tarea 06. Ciclos While
Autor: Luis Miguel Baqueiro

1. Recolectar insectos
2. Encontrar el mayor
3. Salir""")
        numero = int(input("Teclea tu opción: "))
        if numero == 1:
            calcularInsectos()
        elif numero == 2:
            encuentraElMayor()
        elif numero != 3:
            print("ERROR, teclea 1, 2 o 3")
    print("")
    print("Gracias por usar este programa, regresa pronto.")


main()