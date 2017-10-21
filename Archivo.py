#Javier Pascal Flores A013759525
#Encoding: UTF-8

def registro_insectos():
    print(" ")
    print("Bienvenido al programa que registra insectos")
    print("Para salir teclea -1")
    insectos=[]
    while sum(insectos) < 31:
        entrada = int(input("Cuántos insectos recogiste hoy? "))
        insectos.append(entrada)
        print("Despues de %d dia(s) de recolección, llevas %d insectos" % (len(insectos),sum(insectos)))
        if sum(insectos) >= 30:
            sobrante=sum(insectos)-30
            print("Te has pasado con %d insectos" % sobrante)
            print("¡Felicidades, has llegado a la meta!\n")

def calcular_mayor():
    print(" ")
    print("Bienvenido al programa que calcula el mayor")
    numeros = []
    entrada = int(input("Teclea un numero [-1 para salir]: "))
    if entrada == -1:
        print("No hay valor mayor")
    else:
        numeros.append(entrada)
        while entrada != -1:
            entrada = int(input("Teclea un numero [-1 para salir]: "))
            numeros.append(entrada)
        print("El mayor es: ", max(numeros))

def main():
    opcion=0
    while opcion != 3:
        print(" ")
        print("Tarea 06. Ciclos while \nAutor: Javier Pascal Flores\n")
        print("1. Recolectar insectos \n2. Encontrar el mayor \n3. Salir ")
        opcion = int(input("Teclea tu opcion del menu: "))
        if opcion != 1 and opcion != 2 and opcion != 3:
            print("Numero invalido")
        else:

            if opcion == 1:
                registro_insectos()
            elif opcion == 2:
                calcular_mayor()
    print("Gracias por usar el programa.")
main()


