# encondig:UTF-8
#Autor Angel Ramírez Martínez  A01273750
#Descripción: Este programa resgistra el número de insectos recolectados.

# Esta función calcula el número de días e insectos que faltan por recolectar a partir de los que ya se han
# recolectado y del número de días que ha transcurrido.
def recolectarinsectos(contadorDI,dias):
        if contadorDI==30:
            return '''Después de %d día(s) de recolección, llevas %d insectos
Te hace falta recolectar %d insectos
¡Felicidades, has llegado a la meta!
''' % (dias, contadorDI,(30 - contadorDI))
        elif contadorDI < 30 and contadorDI>=0:
            return '''Después de %d día(s) de recolección, llevas %d insectos 
Te hace falta recolectar %d insectos
''' %(dias,contadorDI,30-contadorDI)
        elif contadorDI>30:
            return '''Después de %d día(s) de recolección, llevas %d insectos
Te has pasado con %d insectos
¡Felicidades, has llegado a la meta!
''' % (dias, contadorDI, (contadorDI-30))

# Esta función regresa el valor maximo de una lista que llega como parámetro
def calcularmaximo(lista):
    return 'El mayor es: %d' %max(lista)
# Esta función main es la que corre el programa y en la que se encuentra un menú.
def main():
    menu ="""
    Tarea 06. Ciclos while
    Autor: Angel Ramírez Martínez
    1. Recolectar insectos 
    2. Encontrar el mayor 
    3. Salir"""
    print(menu)
    seleccion = int(input('Ingresa tu opción: '))
    while seleccion!=3:
        if seleccion <1 or seleccion>3:
            print('Opción inválida, ingresar 1,2,3')
            print(menu)
            seleccion = int(input('Ingresa tu opción: '))
        elif seleccion==1:
            print('Bienvenido al programa que registra los insectos que recolectas')
            contadorDI = 0
            dias = 0
            insectos = int(input('¿Cuántos insectos atrapaste hoy? '))
            if insectos >=0:
                while contadorDI<30:
                    dias += 1
                    contadorDI += insectos
                    print(recolectarinsectos(contadorDI,dias))
                    if contadorDI>=30:
                        print(menu)
                        seleccion = int(input('Ingresa tu opción: '))
                    else:
                        insectos = int(input('¿Cuántos insectos atrapaste hoy? '))
            else:
                print('Valor invalido, favor de ingresar un valor válido')
        elif seleccion == 2:
            print('Bienvenido al programa que encuentra el mayor')
            dato = int(input('Teclea un número [-1 para salir]: '))
            lista = []
            while dato != -1:
                lista.append(dato)
                dato = int(input('Teclea un número [-1 para salir]: '))
            if len(lista) == 0:
                print('No hay máximo')
            else:
                print (calcularmaximo(lista))
            print(menu)
            seleccion = int(input('Ingresa tu opción: '))
    print('Gracias por usar este programa, regresa pronto.')
main()