#encoding:UTF-8
#Gerardo Arturo Valderrama Quiroz
#A01374994
#Programa que controla la cantidad de insectos que el usuario atrapa o

import sys

#Funcion que determina cuantos insectos se llevan acumulados, faltan y si se ha alcanado la meta
def administrarinsectos( meta, dias, insectoscontados):
    if meta >= 1:
        texto = """Después de %d día(s) de recolección, llevas %d insectos.
Te hace falta recolectar %d insectos """ % (dias, insectoscontados, meta)
        return texto
    elif meta == 0:
        texto = """Después de %d día(s) de recolección, llevas %d insectos.
Te hace falta recolectar %d insectos
¡Felicidades, has llegado a la meta! """ % (dias, insectoscontados, meta)
        return texto
    else:
        meta = -1*meta
        texto = """Después de %d día(s) de recolección, llevas %d insectos.
Te has pasado con %d insectos
¡Felicidades, has llegado a la meta! """ % (dias, insectoscontados, meta)
        return texto

#Funcion que determina el número mayor
def establecermayor(num, mayor):
    if mayor < num:
        mayor = num
        return mayor
    else:
        return mayor

#Funcion que regula el programa
def main():
    opcion = 0
    while opcion!= 3:
        print("""
Tarea 06. Ciclos While
Gerardo Arturo Valderrama Quiroz

1.Recolectar insectos
2.Encontrar el mayor
3.Salir""")
        opcion = input("Teclea tu opción:")
        if opcion == "1":
            meta = 30
            dias = 0
            insectoscontados = 0
            while meta > 0:
                insectoscapturados = int(input("¿Cuántos insectos atrapaste hoy? "))
                meta -= insectoscapturados
                dias += 1
                insectoscontados += insectoscapturados
                print(administrarinsectos(meta,dias,insectoscontados))

        elif opcion == "2":
            num = input("Teclea un número [-1 para salir]: ")
            mayor = 0
            smayor = ""
            while num != "-1":
                mayor = establecermayor(int(num),mayor)
                smayor = str(mayor)
                num = input("Teclea un número [-1 para salir]: ")
            if len (str(smayor)) > 0:
                print("El mayor es", mayor)
            else:
                print("No hay valor mayor")

        elif opcion =="3":
            print("Gracias por usar este programa, regresa pronto")
            break

        else:
            print("ERROR, Teclea 1, 2 o 3")

main()
