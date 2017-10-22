#encoding UTF-8
#Alejandro Chávez Campos, A01374974
#Este programa contiene distitnas funciones como un contador de insectos y uno que despliega el número mayor.

from math import fabs
def contarInsectos(): #Esta función cuenta los insectos que se va recolectando a lo largo de los días.
    print("Bienvenido al programa que registra los insectos que recolectas")
    diaTotal= 0
    insecto= 0
    while insecto<30:

        insectoRecolectado= int(input("¿Cuántos insectos atrapaste hoy?: "))
        insecto= insecto+insectoRecolectado
        diferencia = 30 - insecto
        diaTotal=diaTotal+1
        if insecto <=30:
            print ("Después de {} dia(s) de recolección, llevas {} insectos".format(diaTotal, insecto))
            print ("Te faltan recolectar {} insectos".format(fabs(diferencia)))
            if diferencia==0:
                print ("¡Felicidades has llegado a la meta!")
        elif insecto>30:
            print ("Después de {} día(s) de recolección llevas {} insectos".format(diaTotal,insecto))
            print("Te has pasado con {} insectos".format(fabs(diferencia)))
            print("¡Felicidades, has llegado a la meta!")


def encontrarMayor():#Esta función determina el número mayor entero positivo a partir de un conjunto que otorga el usuario.
    print("Bienvenido al programa que encuentra el valor")
    lista= []
    numero = int(input("Teclea un número [-1 para salir]: "))
    if numero==-1:
        print("No hay valor mayor")
    if not numero==-1:
        while not numero== -1:
            if numero < -1:
                print("Teclea sólo valores enteros positivos")
                numero = int(input("Teclea un número [-1 para salir]: "))
            if numero>=1:
                lista.append(numero)
                numero= int(input("Teclea un número [-1 para salir]: "))



        numeroMayor = max(lista)
        print("El mayor es: ",numeroMayor)



def main(): #Programa principal
    boton= 10
    while not boton==3:
        print("Tarea 06. Ciclos while")
        print("Autor: Alejandro Chávez Campos")
        print ()
        print("1.Recolectar insectos")
        print("2.Encontrar el mayor")
        print("3. Salir")
        boton=int(input("Teclea tu opción: "))
        print ()
        if boton==1:
            contarInsectos()
        if boton==2:
            encontrarMayor()
        if boton==3:
             print("Gracias por usar este programa regresa pronto")
        if not ((boton==1 or boton==2)or boton==3):
            print ("Error, teclea 1,2 o 3")
        print()
main()