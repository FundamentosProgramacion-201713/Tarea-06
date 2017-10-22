#encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Descripción: Contar insectos con una función, encontrar el número mayor de una lista con una función.
def contarInsectos(insectos,insectosAtrapados,dias):

    while insectos<30:
        insectos = int(input("¿Cuántos insectos recolectaste hoy?:"))
        insectosAtrapados=insectos+insectosAtrapados
        dias+=1
        Faltantes=30-insectosAtrapados
        Sobrantes = insectosAtrapados - 30
        print("Después de", dias, "día(s) de recolección llevas", insectosAtrapados, "insectos")


        if insectosAtrapados>30:
            print("Te pasaste por",Sobrantes, "insectos")
        else:
            print("Te faltan", Faltantes, "insectos")

        if insectosAtrapados>=30:
            print("¡Felicidades, llegaste a la meta!")
            break

def calcularMayor(numero):
    lista=[]
    while numero>=0:
        lista.append(numero)
        numero = int(input("Teclea el número(-1 para salir):"))
    if len(lista)>0:
        print("Mayor:", max(lista))
        list.sort(lista)

    else:
        print("No hay datos")

    return lista

def main():

    print("Bienvenido a este menu")

    print("""
    1. Contar insectos
    2. Número mayor
    3. Salir
      """)

    print("")
    seleccion = int(input("¿Qué desea hacer?:"))

    while seleccion >= 0:
        if seleccion == 1:
            print("Bienvenido al programa que cuenta los insectos recolectados")
            insectos = 0
            insectosAtrapados = 0
            dias = 0

            (contarInsectos(insectosAtrapados, insectos, dias))
            seleccion = int(input("¿Qué desea hacer?:"))

        elif seleccion == 2:
            print("Bienvenido al programa que calcula el número mayor")
            numero = int(input("Teclea el número(-1 para salir):"))
            calcularMayor(numero)
            seleccion = int(input("¿Qué desea hacer?:"))

        elif seleccion == 3:
            print("Adios, gracias por usar este programa")


            break








main()
