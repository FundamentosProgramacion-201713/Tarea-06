#encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Descripción: Contar insectos con una función.

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


def main():
    insectos = 0
    insectosAtrapados = 0
    dias = 0
    print("Bienvenido al programa que cuenta los insectos recolectados")
    print(contarInsectos(insectosAtrapados,insectos,dias))







main()