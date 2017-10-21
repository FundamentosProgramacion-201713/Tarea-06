#Raul Ortiz Mateos
#Encoding: UTF-8

def calcularInsectos():
    print("Bienvenido al programa que registra los insectos que recolectas")
    dias=0#este sera tu contador de dias
    insectos=[]#esta es tu lista donde guardaras todos los numeros que pongas
    insectosTotales=30#tu total de insectos
    while sum(insectos)<insectosTotales:
        i=int(input("el dia de hoy cuantos insectos recogiste? "))
        insectos.append(i)#va ir guardando cada dato que escribas
        dias += 1
        print("despues de",dias,"dia(s),recogiste",sum(insectos),"insectos")#la sumatoria son todos los numeros que tenga
        # la lista

        if sum(insectos)>=insectosTotales: # si es mayor que los insectos totales aqui te dara por cuantos te pasaste
            sumatoria=sum(insectos)-insectosTotales
            print("te has pasado por",sumatoria,"instecto(s)")
            print("has llegado a la meta")


        elif sum(insectos)< insectosTotales:# te ira diciendo cuantos insectos te faltan hasta que llegues al 30
            faltantes = insectosTotales - sum(insectos)
            print("los  faltantes son de ",faltantes,"insectos")

#encoding: UTF-8
#Raul Ortiz Mateos

def calcularNumeros():
    lista = []
    dato = int(input("Teclea un numero[-1 para poder salir]: "))
    while dato != -1:#es te while es donde si es diferente a -1 puede seguir escribiendo numeros y mientras mas numeros
        # escribas se van a ir guardando en tu lista y al final te dara el numero mayor
        lista.append(dato)
        dato = int(input("Teclea un numero[-1 para poder salir]: "))
    if len(lista) > 0:#cuando termines de poner numeros y quieras acabar lo unico que debes de hcer el presionar numeros menores al 0
        print("El numero mayor", max(lista))#te dara el numero mayor de toda la lista que pusiste
    else:
        print("no hay datos")#esto servira por si no pones ningun dato al inicio, te dira que no hay datos


def main():#funcion pricipal

    print("tarea 06")
    print("Autor:Raul ortiz mateos")
    print("Ciclos While")
    print("  ")
    print("1.colectar insectos")
    print("2.encontrar el Mayor")
    print("salir del menu")
    print("   ")
    numero=int(input("que numero desea poner? "))
    while not numero==3:
        if numero ==1:
            print("usted eligio calcular insectos")
            calcularInsectos()
            print("  ")
        elif numero==2:
            print("usted eligio numero mayor")
            calcularNumeros()
            print("   ")
        else:
            numero!=1 and numero!=2 and numero!=3
            print("ERROR, escriba un numero que sea solo de 1 a 3")

            print("     ")

        print("tarea 06")
        print("Autor:Raul ortiz mateos")
        print("Ciclos While")
        print("  ")
        print("1.colectar insectos")
        print("2.encontrar el Mayor")
        print("3.salir del menu")
        print("   ")
        numero = int(input("que numero desea poner? "))


    print("nos vemos")


main()