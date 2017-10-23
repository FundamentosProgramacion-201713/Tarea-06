# encoding UTF-8
# Autor: Javier León Alcántara
# Tarea 06, Menu para acceder a diferentes ejercicios.

def recolectarInsectos():

    print("Bienvenido al programa que registra los insectos que recolectas")

    sumaInsectos = 0  #Comienza con cero insectos
    numDias = 1    #Primer día

    while sumaInsectos < 30:  #Mientras la suma de insectos sea menor que treinta

        insectos = int(input("¿Cuántos insectos atrapaste hoy? "))


        suma = sumaInsectos + insectos   # va a sumar los insectos anteriores con los nuevos
        faltantes = 30 - suma    #Calcula los insectos faltantes para 30

        if suma < 0 :          #Si el número de insectos es menor que cero el dato no es valido
            print("Error, escribe un número valido")
            suma = 0              #Mantiene los datos de suma y el número de días
            numDias = 0

        elif suma < 30 and suma >= 0:      #Si el número de insectos es menor que 30, y mayor que 0 calcula los insectos y cuantos faltan.
            print("Después de", numDias, "día(s) de recolección, llevas", suma, "insectos")
            print("Te hace falta recolectar", faltantes, "insectos")


        elif suma == 30:  #Si el número es 30 va a calcular los datos y mostrar un mensaje
            print("Después de", numDias, "día(s) de recolección, llevas", suma, "insectos")
            print("Te hace falta recolectar", faltantes, "insectos")
            print("¡Felicidades, has llegado a la meta!")
            print("\r")

        elif suma >30:   #Si el número de insectos es mayor que treinta, va a calcular los insectos sobrantes
            print("Después de", numDias, "día(s) de recolección, llevas", suma, "insectos")
            print("Te has pasado con",abs(faltantes) ,"insectos")
            print("¡Felicidades, has llegado a la meta!")
            print("\r")

        sumaInsectos = suma    # suma el numero de insectos para wue se vuelva a contemplar
        numDias = numDias + 1  #Suma los días



def encuentraMayor():
    print("Bienvenido al programa que encuentra el mayor")
    lista = []    #Lista
    numero = int(input("Teclea un número [-1 para salir] "))

    while numero != -1:   #Mientras el numero sea mayor a "-1"
        lista.append(numero)  #Agrega el número a la lista
        numero = int(input("Teclea un número [-1 para salir] "))  #Vuelve a mostrar la pregunta
    if len(lista) != 0:  #si el número de valores que hay en la lista es diferente de 0
        mayor = max(lista)     #busca el mayor
        print("El mayor es ", mayor)  #imprime el mayor
        print("\r")
    else:
        print("No hay valor mayor ")
        print("\r")


def main():   #Menu

    eleccion = 1  #Se le da a valor a elección no importa cual, sólo que sea diferente de 3
    while eleccion != 3:

        print("Tarea 06. Ciclos While")    #Se muestran los datos
        print("Autor: Javier León Alcántara")
        print("\r")
        print("1. Recolectar insectos")
        print("2. Encontrar el mayor")
        print("3. Salir")
        eleccion = int(input("Teclea tu opción: "))  #El usuario elige lo que quiere hacer

        if eleccion == 3:    #Se ejecuta la función acorde al numero que elijió
            print("\r")
            print("Gracias por usar este programa, regresa pronto")

        elif eleccion == 1:
            print("\r")
            recolectarInsectos()

        elif eleccion == 2:
            print("\r")
            encuentraMayor()

        elif eleccion < 1 or eleccion > 3:   #Si el numero no esta entre el 1,2 o 3 imprime mensaje de error
            print("ERROR, teclea 1, 2 o 3")
            print("\r")
main()











