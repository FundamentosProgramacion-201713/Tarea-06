#encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Descripción: Contar insectos con una función, encontrar el número mayor de una lista con una función.

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
    print("Bienvenido al programa que calcula el número mayor")
    numero = int(input("Teclea el número(-1 para salir):"))
    print(calcularMayor(numero))




main()