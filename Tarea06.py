#uncoding: UTF-8
#Autor: Ana María López Soto
#Descripción: El programa calcula la cantidad de insectos recolectados y el numero mayor de un conjunto.

def calcularTotlalInsectos():
    print("Bienvenido al programa que registra los insectos que recolectas ")
    total_insectos = 0 #Contador de insectos
    dias_transcurridos = 0 #Contador de días transcurridos
    meta = 30 #Total al que se tiene que llegar de insectos
    while total_insectos < meta:
        insectos_mas = int(input("¿Cuántos insectos atrapaste hoy? ")) #Cuantos insectos recolecta el usuario
        total_insectos += insectos_mas #Adición al contador de insectos con los que ingresa el usuario
        dias_transcurridos += 1 #Adición al contador de días
        insectos_faltantes = meta - total_insectos #Meta de insectos menos los insectos ya recolectados
        insectos_sobrantes = total_insectos - meta #Insectos ya recolectados menos la meta
        print("Después de", dias_transcurridos,  "día(s) de recolección, llevas", total_insectos, "insectos")
        if total_insectos < 30: #Si aún le falta recolectar
            print("Te hace falta recolectar", insectos_faltantes, "insectos")
        else: #Si ya llego o supero la meta de insectos
            print("Te has pasado con", insectos_sobrantes, "insectos")
            print("¡Felicidades, has llegado a la meta!")

def esMayor():
    print("Bienvenido al programa que encuentra el mayor")
    lista = []#Lista vacía
    dato = int(input("Teclea un número [-1 para salir]: ")) #Datos que ingresa el ususario
    while dato != -1: #El -1 indica la salida del programa
        lista.append(dato) #Agregar dato ingresado a la lista
        dato = int(input("Teclea un número [-1 para salir]: ")) #Datos que ingresa el ususario

    if len(lista) > 0: #Si la lista contiene datos
        print("El mayor es: ", max(lista)) #Comparación entre datos ingresados a la lista
    else:
        print("No hay datos") #Resultado si no se ingesa ningún dato


def main():
    print("Tarea 06. Ciclos while")
    print("Autor: Ana María López Soto")
    print("")
    print("1. Recolectar insectos")
    print("2. Encontrar el mayor")
    print("3. Salir")
    selección = int(input("Teclea tu opción:"))

    terminar = False

    while not terminar:
        if selección == 1:
            print(" ")
            calcularTotlalInsectos()
            print(" ")
            selección = int(input("Teclea tu opción:"))
        elif selección == 2:
            print(" ")
            esMayor()
            print(" ")
            selección = int(input("Teclea tu opción:"))
        elif selección == 3:
            print("Gracias por usar este programa, regresa pronto.")
            terminar = True
            quit()
        else:
            print("ERROR, teclea 1, 2 o 3.")
            selección = int(input("Teclea tu opción:"))
            print(" ")

main()
