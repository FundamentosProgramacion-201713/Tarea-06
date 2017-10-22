# Autor: Mónica Monserrat Palacios Rodríguez
# UTF-8
# Tarea 6

#Función que calula los insectos
def recolectarInsectos():

    insectos = 0
    dias = 0

    print("Bienvenido al programa que registra los insectos que recolectas")#Se da la bienvenida

    while insectos < 30: #Se abre ciclo while para que se repita hasta que se indique lo contrario
        numInsectos = int(input("¿Cuántos insectos atrapaste hoy? "))
        dias = dias+1
        insectos = insectos + numInsectos
        insectosFaltantes = 30 - insectos
        insectosSobrantes = insectos - 30

        print ("Después de %d día(s) de recolección, llevas %d insectos" %(dias, insectos))

        if insectos < 30: #Ifs para dar los comentarios adecuados o indicar que ganó
            print ("Te hace falta recolectar %d insectos" %insectosFaltantes)

        else:
            print("Te has pasado con %d insectos" % insectosSobrantes)

    print("¡Felicidades, has llegado a la meta!")#Si sale de while es que ha llegado a la meta
    print(" ")


#Función para encontrar el mayor
def encontrarElMayor():
    print("Bienvenido al programa que encuentra al mayor")#Bienvendia al programa
    numeros = []#Se crea la lista
    num = int(input("Teclea un múmero [-1 para salir] "))
    if num == -1:
        print("No hay valor mayor")
    elif num < -1:
        print("Sólo números enteros positivos por favor")
    else:
        while num != -1:
            numeros.append(num)
            num = int(input("Teclea un múmero [-1 para salir] "))
        print ("El mayor es: ", max(numeros))
        print(" ")

#Función principal
def main():
#Letreros de bienvenida y explicación
    print ("Tarea 06. Ciclos While")
    print ("Autor: Mónica Monserrat Palacios Rodríguez")
    print(" ")
    print ("1. Recolectar insectos")
    print ("2. Encontrar el mayor")
    print ("3. Salir")
    opcion = int(input("Teclea tu opción: "))
    print(" ")

    while 1:#Comienza el while del menú
        if opcion == 1:
            recolectarInsectos()
        elif opcion == 2:
            encontrarElMayor()
        elif opcion == 3:
            print("Gracias por usar este programa, regresa pronto")
            break
        else:
            print("ERROR, teclea 1, 2 ó 3")
            break

main()