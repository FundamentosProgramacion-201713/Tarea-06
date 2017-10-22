#Encoding UTF-8
#Anaid Fernanda Labat González
#Descripción-1: Este programa permite al usuario ingresar cuántos insectos captura por día y le indica cuántos le faltan para llegar la meta y al hacerlo, lo felicita


def capturarInsectos():
   print("Bienvenido al programa que registra los insectos que recolectas") # Bienvenida
   valor = True
   insectosCap = int(input("¿Cuántos insectos capuraste el día de hoy?: ")) #Insectos recolectados por el usuario
   d = 0

   while valor:
    d += 1
    print("Despues de %d día(s) de recolección, llevas: %d insectos recolectados" % (d, insectosCap)) #Imprime la cantidad de insectos capturados por el usuario

    if insectosCap >= 30:
        print("Te has pasado por:", insectosCap - 30, "insectos") #Indica cuántos insectos más de los requeridos han sido recolectados
        print("¡Felicidades, has llegado a la meta!")
        valor = False
    elif insectosCap == 30:
        print("Te hace falta recolectar:", 30 - insectosCap, "insectos") #Indica cuántos insectos faltan ára la meta
        valor = False
    else:
        print("Te hacen falta", 30 - insectosCap, "insectos")
        insectosCap += int(input("¿Cuántos insectos capuraste hoy?:"))

#Descripción-2: Indica el número mayor entre una lista de números dada por el usuario
def encontrarNMayor():
    print(("Bienvenido al programa que encuentra el mayor"))
    numeros = []  # Lista con valores ingresados por el usuario
    n = int(input("Teclea un numero [-1 para salir]: "))  # El usuario ingresa numeros
    if n == -1: #Salir
        print("No hay valor mayor")
    else:
        while n != -1:
            numeros.append(n)
            numero = int(input("Teclea un número [-1 para salir]: "))
            print("El número mayor es: ", max(numeros)) #Indica cuál es el número mayor

def main(): #Llama a las funciones cuando el usuario elige una opción del menú
    seleccionar = 0
    while seleccionar >= 0:
        print("""Tarea 06 - Ciclos While 
Autor: Anaid Fernanda Labat González         
        1. Recolectar insectos 
        2. Encontrar el mayor 
        3. Salir 
        """)
        seleccionar = int(input("Teclea tu opción:"))
        if seleccionar == 1: # Llama a la función para saber cuántos insectos han sido capturados
            capturarInsectos()
        elif seleccionar == 2: #Llama a la función para saber cuál es el número mayor
            encontrarNMayor()
        elif seleccionar == 3: #Termina el programa agradeciendo
            print("")
            print("Gracias por usar este programa, regresa pronto.")
        else:  # Cualquier número diferente es considerado marca como error.
            print("")
            print("ERROR, teclea 1,2,3")
            print("")
main()
