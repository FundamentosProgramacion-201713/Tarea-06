#encoding: UTF-8
#Autor: Omar Israel Galván García A01745810
#Este programa usa el ciclo while y listas para resolver probelmas

def calcularInsectos():          #función contar insectos
    insectosTotal = 0            #se inicia una variable que acumulará los insectos
    dias = 0                     #se inicia una variable-contador para los días
    insectosRecolectados = 0     #el número de insectos del usuario por día

    print("Bienvenido al progama que registra los insectos que recolectas") #se da la  bienvenida al programa
    insectosTotal += insectosRecolectados     #se comienzan a contar los insectos

    while insectosTotal < 30:    #Ciclo While mientras que el #de insectos sea menor que 30 ejecuta lo de abajo
        insectosRecolectados = int(input("¿Cuántos insectos atrapaste hoy?")) #pregunta al usuario cuántos insectos recolectó en el día
        insectosTotal += insectosRecolectados  #se suman a los insectos de días pasados
        dias += 1                #el día incrementa en 1 cada vez que pasa por la pregunta
        insectosRestantes = 30-insectosTotal  #calcula los insectos que le faltan para cumplir su meta

        if insectosTotal<30:    #si los insectos totales son menores a 30 ejecuta las siguientes instrucciones:
            print("Después de %d día(s) de recolección, llevas %d insectos."%(dias,insectosTotal)) #actualiza la información de la recolección
            print("Te hace falta recolectar %d insectos"%(insectosRestantes)) #actuzliza la información del número de insectos restantes

        if insectosTotal >= 30: #si los insectos recolectados son mayores a la meta (30) ejecuta lo siguiente:
         print("Después de %d día(s) de recolección, llevas %d insectos" % (dias, insectosTotal)) #actualiza la información del número de insectos
         print("Te has pasado con %d insectos" % (insectosTotal - 30))  #calcula el número de insectos que recolectó de más
         print("¡Felicidades, has llegado a la meta!")   #imprime una felicitación
         print("\n")             #espacio

    main() #una vez alcanzada la meta vuelve al menu principal

def encontrarMayor():    #función que calcula  el mayor de varios números dados por el usuario
    lista = []    #una lista vacia para comenzar a introducir valores
    print("Bienvenido al programa que encuentra al mayor") #Da la bienvenida al programa

    while lista != 0:  #mientras que el contenido de la lista sea diferente de cero se ejecuta lo siguiente:
        numero = int(input("Teclea un número [-1 para salir]: "))  #pregunta un número al usuario
        lista.append(numero) #guarda el valor de "número" en el espacio correspondiente de lista

        if numero == -1 and len(lista)>1:  #condicional si el conjunto de números dados es mayor a uno y se pide el resultado con -1
           print("El mayor es:",max(lista))  #imprime el valor máximo que tiene lista en sus espacios
           print("\n"*2)         #espacio
           main()  #una vez que regresa un número máximo vuelve al menú principal
        if numero == -1 and len(lista) == 1:  #si la longitud de la lista es uno y se pide respuesta, entonces no hay un valor mayor
          print("No hay valor mayor")  #imprime una advertencia
          print("\n"*2)  #espacio
          main()

def main():  #función principal

    print("Tarea 06. Ciclos While")
    print("Autor: Omar Israel Galván García")
    print("1.Recolectar insectos" #despliega el menú principal
        "\n"
          "2.Encontrar el mayor"
        "\n"
          "3.Salir")
    opcion = int(input("Teclea tu opción: "))  #pregunta al usuario por la opción que prefiere
    print("\n"*2)
    if opcion >= 4:     #si es otro número diferente de 1, 2 o 3 imprime una advertencia
        print("ERROR,teclea 1, 2 o 3")  #imprime la advertencia

    while opcion <=3:  #mientras que la opción seleccionada sea menor o iguala 3 se ejecuta el menú
        if opcion == 1:
            calcularInsectos()
        elif opcion == 2:
         encontrarMayor()
        elif opcion == 3:
            print("Gracias por usar este programa, regresa pronto.")  #imprime despedida
            print("\n")  #espacio
            break  #termina el programa


main()





