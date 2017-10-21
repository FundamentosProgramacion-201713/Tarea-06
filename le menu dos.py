def insectos():
    print("Bienvenido al programa que registra los insectos que recolectas")
    dias=1
    insec=int(input("Cuantos insectos atrapaste hoy?  "))
    while insec<=30:
        if insec >=30:
            print("despues de", dias, "dia(s) de recoleccion, llevas", insec, "insectos")
            suma= insec-30
            print("Te has pasado con", suma, "insectos")
            print("Felicidades has llegado a la meta ")
            break
        elif insec <30:
            print("despues de",dias ,"dia(s) de recoleccion, llevas", insec, "insectos")
            dias+=1
            falta=(insec-30)*-1
            print("Te hacen falta recolectar", falta)
            insec+=int(input("Cuantos insectos atrapaste hoy?  "))


def capturarDatos():
    print(("Bienvenido al programa que encuentra el mayor"))
    lista=[]
    dato = int(input("Teclea un numero [-1 para salir]: "))
    if dato==-1:
        print("No hay valor mayor")
    else:
        while dato!=-1:
            lista.append(dato)
            dato=int(input("Teclea un numero [-1 para salir]: "))
        print("El mayor es: ",max(lista))


def main():
    print("1. Recolectar insectos ")
    print("2. Encontrar el mayor")
    print("3. Salir")
    numero=int(input("Dar un numero del 1 al 3 :"))
    while numero!=3:
        if numero==1:
            insectos()
        if numero==2:
            capturarDatos()
        print("1. Recolectar insectos ")
        print("2. Encontrar el mayor")
        print("3. Salir")
        numero = int(input("Dar un numero del 1 al 3 :"))
main()


