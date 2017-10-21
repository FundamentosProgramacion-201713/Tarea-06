#UTF-8
#Natalia Meraz Tostado
#Tarea 6

def esMayorOMenor():
    lista = []
    dato = int(input("Teclea un valor [-1 para salir]: "))
    while dato != -1:
        lista.append(dato)
        dato = int(input("Teclea un valor [-1 para salir]: "))

    if len(lista) > 0:
        print("El mayor es: ", max(lista))

    else:
        print("No hay valor mayor")

def main():
    print("Bienvenido al programa que encuentra el mayor")
    esMayorOMenor()

main()