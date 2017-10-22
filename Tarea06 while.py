# Encoding: UTF-8
# Autor: Gabriela Mariel Vargas Franco
#Un niño tiene como meta recolectar 30 onsectos. Cada día recolecta cierto número de insectos.
#Función que pregunta al usuario cuántos insectos recolectó e imprima

def recolectarInsectos():
    print("Bienvenido al programa que registra los insectos que recolectas.")
    dias=0

    insectosRec=int(input("Cuántos insectos recolectaste hoy?"))

    while insectosRec<30:
        dias=dias+1
        print("Después de %d día(s) de recolección, llevas %d insectos"% (dias,insectosRec))
        insectosFaltan=30-insectosRec
        print("Te hace falta recolectar ",insectosFaltan, "insectos")
        if insectosRec<=30:
            insectos=int(input("Cuántos insectos recolectaste hoy?"))
            insectosRec=insectosRec+insectos
    #if para ver cuántos insectos le sobran
    if insectosRec>=30:
        dias=dias+1
        insectosSobran=insectosRec-30
        print("Después de %d día(s) de recolección, llevas %d insectos"% (dias,insectosRec))
        print("Te has pasado con ",insectosSobran, "insectos")
        print("¡Felicidades, has llegado a la meta!")



    main()

def encontrarMayor():
    mayor=0
    print("Bienvenido al programa que encuentra el mayor")
    numero=int(input("Teclea un número [-1 para salir]: "))
    if numero==-1:
        print("No hay valor mayor")
    else:
        while numero>-1:
#if para ver cual es el mayor del conjunto de datos
            if numero>=mayor:
                mayor=numero
            else:
                mayor=mayor
            numero=int(input("Teclea un número [-1 para salir]:"))
        print("El mayor es:", mayor)

    main()

def main():
    print("Tarea 06. Ciclos while")
    print("Autor:Gabriela Mariel Vargas Franco")
    print("1. Recolectar insectos")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion=int(input("Teclea tu opción:"))
    terminar=False

    while opcion!=terminar:
        if opcion==1:
            recolectarInsectos()
        elif opcion==2:
            encontrarMayor()
        else:
            print("Gracias por usar este programa, regrese pronto")
        break #FIN
main()


