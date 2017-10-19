# encoding: UTF-8
# Autor: Edgar Alexis González Amador

#Función que permite al usuario instroducir la cantidad d einsectos recolectados por día y saber en que momento se llega a la meta de recoleccion
def RecolectarInsectos():
    print("Bienvenido al programa que registra los insectos que recolectas")
    dias = 0
    insectos = 0
    meta = 30
    #Este while permite preguntar al usuario los insectos atrapados hasta que se consiga la meta
    while(insectos < 30):
        dias += 1
        atrapados = int(input("¿Cuántos insectos atrapaste hoy? "))
        insectos = insectos + atrapados
        print("Después de %d día(s) de recolección, llevas %d insectos"%(dias, insectos))
        faltantes = meta - insectos
        if (faltantes >= 0):
            print("Te hace falta recolectar %d insectos"%faltantes)
        else:
            faltantes = faltantes * -1
            print("Superaste tu meta por %d"%faltantes)
    print("¡Felicidades, has llegado a la meta!")


#Función que permite calcular de un numero indeterminado de entradas cual es el numero mayor introducido
def CalcularMayor():
    print("Bienvenido al programa que encuentra el mayor")
    numero = 0
    numeroMayor = 0
    #Este while permite al usuario introducir un numero indeterminado de valores hasta que se introduzca -1
    while(numero != -1):
        numero = int(input("Teclea un número [-1 para salir]: "))
        if (numero >= 0):
            if (numero > numeroMayor):
                numeroMayor = numero
        else:
            print("El numero no puede ser negativo")
    if (numeroMayor == 0):
        print("No hay valor mayor")
    else:
        print("El mayor es: %d"% numeroMayor)
#Función main, que contiene un menu para poder acceder a cualquiera de las funciones anteriores.
def main():
    print("Tarea 06. Ciclos while\nAutor: Edgar Alexis González Amador")
    print("1. Recolectar insectos\n2. Encontrar el mayor\n3. Salir")
    eleccion = 0
    #Este while permite introducir al usuario los valores diferentes de 3 la cantidad de veces que desee, y salir cuando se teclee 3
    while(eleccion != 3):
        eleccion = int(input("Teclea tu opción: "))
        if (eleccion == 1):
            RecolectarInsectos()
        elif (eleccion == 2):
            CalcularMayor()
        else:
            print("Debes elegir una de las opciones del menú")
    print("Adiós")
#Se ejcuta la f1uncion main para poder correr el programa
main()