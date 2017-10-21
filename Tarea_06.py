# encoding: UTF-8
# Autor: Pedro Cortés Soberanes
# Tarea 06: Ciclcos


###################################################################################################
 # RECOLECTAR INSECTOS

def recolectarInsectos():
    print ("Bienvenido al programa que registra los insectos que recolectas")
    listaInsectos = []
    insectos = 0
    meta = 30

    while sum(listaInsectos) != meta and sum(listaInsectos) < meta:


        insectos  = int(input("¿Cuántos insectos atrapaste hoy? "))
        listaInsectos.append(insectos)
        print ("Después de %s día(s) de recolección, llevas %d insectos" %(len(listaInsectos),sum(listaInsectos)))

        if sum(listaInsectos) < meta:
            print("Te faltan recolectar %d insectos" % (30 - sum(listaInsectos)))

        if sum(listaInsectos) > meta:
            print ("Te has pasado con %d insectos " % (sum(listaInsectos)-30))
            print("¡Felicidades, has llegado a la meta!")

        if sum(listaInsectos) == meta:
            print("Te faltan recolectar %d insectos" % (30 - sum(listaInsectos)))
            print ("¡Felicidades, has llegado a la meta!")


###################################################################################################
 # ENCONTRAE EL NÚMERO MAYOR

def encontrarMayor():
    print("Bienvenido al programa que encuentra el mayor")
    listaMayor = []
    numero = int(input("Teclea un número [-1 para salir]: "))

    while numero!= -1:
        listaMayor.append(numero)
        numero = int(input("Teclea un número [-1 para salir]: "))

    if len(listaMayor) > 0:
        print ("El mayor es: ", max(listaMayor))
    else:
        print("No hay valor mayor")

###################################################################################################
 #FUNCIÓN MAIN & MENU

def main():
    opcion = -1
    while opcion != 3:
        print ("Tarea 06. Ciclos while")
        print("""Autor: Pedro Cortés Soberanes 
         """)
        print("1. Recolectar Insectos ")
        print("2. Encontrar el mayor")
        print("3. Salir")
        opcion = int(input("Teclea tu opción: "))
        if opcion == 1:
            recolectarInsectos()
        elif opcion ==2:
            encontrarMayor()
        elif opcion == 3:
            print ("Gracias por usar este programa, regresa pronto.")

main()