#UTF-8
#Oscar Zuñiga Lara
#A01654827

def recogertInsectos():
    insectos = 0
    dia = 0
    while insectos in range(0,30):
        recogidos = int(input("¿Cuántos insectos atrapaste hoy?"))
        dia = dia + 1
        insectos = insectos + recogidos
        print("Después de " , dia, "día(s) de recolección, llevas" , insectos ,  "insectos")
        if insectos > 30:
            insectosPasados = insectos - 30
            print("Te has pasado con ", insectosPasados,"Insecto(s)" )
        else:
            insectosFaltantes = 30 - insectos
            print("Te hace falta recoger" , insectosFaltantes , "insectos")
    print("¡FELICIDADES!, llegaste a la meta")

def mayorNumero():
    print("Bienvenido al programa que encuentra el mayor  ")
    numero = int(input("Teclea un número [-1 para salir]:"))
    if numero > 0:
        lista = []
        while numero > -1:
            lista.append(numero)
            numero = int(input("Teclea un número [-1 para salir]:"))
        print("El mayor numero es : " , max(lista))
    else:
        print("No hay numeros")

def main():
    usuario = 0
    while usuario > -1:
        print("1. Recolectar insectos")
        print("2. Encontrar el mayor")
        print("3. Salir ")
        usuario =  int(input("Teclea tu opción:"))

        if usuario == 1:
            recogertInsectos()
        elif usuario == 2:
            mayorNumero()
        else:
            print("Adios")
            usuario = -2

main()
