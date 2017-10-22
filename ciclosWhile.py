# encoding: UTF-8
# Autor: Angel Roberto Pesado Bartolo A01374942
# Tarea 6 empleando ciclos while


def capturarInsectos():#definimos la función
    print("Bienvenido al programa que registra los insectos que atrapaste ")#Informamos que hace el programa
    insectos=[]#Definimos una lista
    dias=0 #Definimos el inicio de los días

    while sum(insectos)<=30: #Mientras los insectos sean menores o iguales a 30 hará las siguientes lineas
        insectosCapturados = int(input("¿Cuántos insectos atrapaste hoy?: "))#Pedimos al usuario los numeros de insectos capturados la primera vez
        insectos.append(insectosCapturados)#Guardamos el numero en la lista creada
        dias+=1#sumamos un día después de capturar cierto numero de insectos
        print("Después de %d días llevas %d insectos capturados" %(dias,sum(insectos)))#Mostramos al usuario cuantos insectos cuantos insectos lleva y cuantos días han transcurrido

        if sum(insectos) <=30: #Sí la sumatoria de los insectos es menor a 30
            insectosNoCapturados=30-sum(insectos)#obtenemos cuantos insectos faltan capturar
            print("Los insectos que faltan capturar son: ", insectosNoCapturados)#Informamos al usuario cuantos insectos le faltan por capturar
            if insectosNoCapturados==0:#sí ya no hay insectos por capturar
                return print("Felicidades, has llegado a la meta","\n")#informamos al usuario que ha llegado a la meta
        elif sum(insectos)>30:#sí los insectos que teclea el usuario es mayor a 30
            insectosExcedidos=sum(insectos)-30#obtenemos por cuantos insectos se ha pasado
            print("Felicidades, has llegado a la meta\nLos insectos por los que te pasaste fueron:",insectosExcedidos,"\n")#informamos al usuario que ha llegado a la meta y por cuanto se paso



def calcularNumeroMayor():#Definimos la función
    print("Bienvenido al programa que encuentra el numero mayor")
    num=int(input("Dame un numero[-1 para salir del programa]: "))#Pedimos al usuario el numero
    lista=[]#creamos una lista en blanco
    while num !=-1 :#mientras el numero sea diferente a -1 hará las siguientes lineas
        lista.append(num)#Guardamos el numero en la lista
        num=int(input("Dame un numero[-1 para salir del programa]: "))#pedimos un nuevo numero
    if len(lista)<=0:#sí el usuari teclea -1 imprime que no hay datos
            print("No hay datos, hasta la proxima\n")
    else:
            print("El numero mayor de los numeros que me diste es: ",max(lista),"\n")#informamos al usuario que numero de su lista es el mayor.


def main():#definimos la función
    salirMenu=True
    while salirMenu:#mientras el menu sea seleccionable hará lo siguiente
        print("Tarea 06.Ciclos while\nAngel Roberto Pesado Bartolo A01374942\n1.-Recolectar Insectos\n2.-Encontrar el mayor\n3.-Salir")
        desicion=int(input("¿Qué deseas realizar?: "))#Pedimos al usuario que desea hacer
        if desicion <=0 or desicion >3:#indicamos que si la desicion del usuario es menor a 0 o mayor a 3 indique que está en error y eliga de nuevo
            print("ERROR, teclea 1,2,3\n")
        elif desicion==1:#si la decisión es 1
            capturarInsectos()#ejecuta la función capturarInsectos
        elif desicion==2:#si la desición es 2
            calcularNumeroMayor()#ejecutta la función calcularNumeroMayor
        elif desicion==3:#si la desición es 3
            return print("Gracias por usar este programa, regresa pronto")#imprime este anuncio

main()#llamamos a la función main