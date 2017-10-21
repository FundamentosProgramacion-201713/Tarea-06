#encoding: UTF-8
#Autor: Jean Paul Esquivel Lobato
#Matrícula: A01376152
#Descripcion: Realizar ciclos con while usando contadores


def cInsectos():
    print("Bienvenido al programa que registra los insectos que recolectas")
    val=True
    insect=int(input("¿Cuántos insectos capuraste el día de hoy? "))
    d=0
    while val:
        d+=1
        print("Despues de %d día(s) de recolección, llevas %d insectos recolectados"%(d,insect))
        if insect >= 30:
            print("Te has pasado por",insect-30,"insectos")
            print("¡Felicidades, has llegado a la meta!")
            val=False
        elif insect==30:
            print("Te hace falta recolectar",30-insect,"insectos")
            print("¡Felicidades, has llegado a la meta!")
            val=False
        else:
            print("Te hacen falta",30-insect,"insectos")
            insect += int(input("¿Cuántos insectos capuraste hoy? "))

def encuentraM():
    print("Bienvenido al programa que encuentra el numero mayor")
    listaN=[]
    valorE=int(input("Teclea un número [-1 para salir]: "))
    if valorE!=-1:
        while valorE!=-1:
            listaN.append(valorE)
            valorE = int(input("Teclea un número [-1 para salir]: "))
        print("El numero mayor es: ",max(listaN))

    else:
        print("No hay valor mayor")

def main():
 menu=1
 while menu ==1:
    print('''Tarea.06 Ciclos While
    Autor: Jean Paul Esquivel
    1. Recolectar Insectos
    2. Encontrar el Mayor
    3. Salir''')
    usuario=int(input("Teclea la opción que quieras realizar: "))
    if usuario == 3:
        menu = 0
        print("Gracias por usar este programa, regresa pronto.")
    elif usuario==1:
       cInsectos()
    elif usuario==2:
       encuentraM()
    else:
        print("ERROR, teclea 1, 2 o 3")

main()
