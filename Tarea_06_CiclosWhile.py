# Autor: Saúl Rodrigo Toral luna
# Matrícula: A01745007

# El programa por medio de ciclos while resolverá los problemas por medio de la selección del usuario
# Si escoge una opción como 1 0 2 realiza el ejercicio
# Si escoge como opción 3 el programa sale
# Pero si escoge algun otro número marca error y pide al usuario corregir su opción



# La función por medio de contadores y un ciclo while analiza la cantidad de insectos que ha recolectado en un plazo de tiempo
def recolectarInsectos():
    # Se generan contadores y acumuladores
    insecto = 0
    dias = 0
    print("Bienvenido al programa que registra los insectos que recolectas")
    while insecto < 30:
        insectos_Recolectados = int(input("¿Cuántos insectos atrapaste hoy?: "))
        if insectos_Recolectados < 0:
            print("Ingresa números positivos")
        else:
            dias += 1
            insecto +=  insectos_Recolectados
            faltantes = 30 - insecto
            print("Despues de %d día(s) de recolección, llevas %d insecstos" % (dias, insecto))
            if insecto <= 30:
                print("Te hace falta recolectar %d insectos" % faltantes)
            else:
                print("Te has pasado con %d insectos" % (insecto-30))
    print("¡Felicidades, has llegado a la meta!")
    print("")
    mensaje = ""
    return mensaje

# La función encuentra el mayor número de una lista en donde se guardan los números que ingresa el usuario
def encontrarElMayor():
    print("")
    print("Bienvenido al programa que encuentra el mayor")
    lista = []
    valor = int(input("Teclea un número [-1 para salir]: "))
    while valor != -1:
        lista.append(valor)
        valor = int(input("Teclea un número [-1 para salir]: "))
    if len(lista) > 0:
        print("El mayor es: ", max(lista))
    else:
        print("No hay valor mayor")
    print("")
    mensaje = ""
    return mensaje

# Función principal donde se hace el menú del programa por medio de una función while
def main():
    ejercicio = True
    while ejercicio == True:
        print("Tarea 06. Ciclos while")
        print("Autor: Saúl Rodrigo Toral Luna")
        print("")
        print("1. Recolectar insectos")
        print("2. Encontrar el mayor")
        print("3. Salir")
    #Ingreso de la opción a desarrollar
        opcion = int(input("Teclea tu opción: "))
        print("")
    # Toma de decisión
        if opcion == 1:
            print(recolectarInsectos())
        elif opcion == 2:
            print(encontrarElMayor())
    # Si elige el 3 el programa rompe el ciclo while
        elif opcion == 3:
            ejercicio = False
            print("Gracias por usar este programa, regresa pronto.")
        else:
            print("ERROR, teclea 1, 2 o 3")
            print("")

main()