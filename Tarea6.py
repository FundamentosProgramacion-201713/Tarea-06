#Encoding: UTF-8
#Autor: Joaquin Rios Corvera A01375441

#Esta función calcula cuántos insectos se necesitan para llegar a 30 y cuenta los días que han pasado
def recolectarInsectos():
    insectos = 0
    dias = 0

    while insectos < 30:
        insectosPorDia = int(input("¿Cuántos insectos atrapaste hoy? "))
        dias += 1
        insectos += insectosPorDia
        restantes = 30 - insectos
        print("Después de %d día(s) de recolección, llevas %d insectos" %(dias, insectos))
        if insectos <= 30:
            print("Te hace falta recolectar %d insectos" %restantes)
        else:
            print("Te has pasado con %d insectos"%(insectos-30))
    print("¡Felicidades, has llegado a la meta!")
    print("")
#Esta función toma una serie de números y regresa el mayor
def calcularMayor():
    x = 0
    numeros = []
    print("Bienvenido al programa que encuentra el mayor")
    while x!=-1:
        x = int(input("Teclea un número [-1 para salir]:"))
        if x < -1:
            print("Solo se tomarán en cuenta valores positivos")
        numeros.append(x)
    numeros.sort(reverse=True)
    mayor = numeros[0]
    if mayor==-1:
        print ("No hay valor mayor")
    else:
        print("El mayor es: %d" %mayor)
    print("")

def main():
    x = 0
    while x != 3:
        print('''Tarea 06. Ciclos while
Autor: Joaquin Rios Corvera
              
1. Recolectar insectos
2. Encontrar el mayor
3. Salir''')
        x = int(input("Teclea tu opción: "))
        print("")
        if x == 1:
            recolectarInsectos()
        elif x == 2:
            calcularMayor()
        elif x == 3:
            print("Gracias por usar este programa, regresa pronto.")
        else:
            print("ERROR, teclea 1, 2 o 3")

main()