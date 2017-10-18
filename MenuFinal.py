#encoding: UTF-8
#Autor Aaron Villanueva

introduccion="Tarea 06. Ciclos While"
autor="Autor Aaron Villanueva"

def recolectarinsecto():
  print("Bienvenido al programa que registra los insectos que recolectas")
  contador=0
  insectosprevios=0
  meta=30
  activo=True
  while activo==True:
    insectos=int(input("¿Cuántos insectos atrapaste hoy?" ))
    contador+=1
    insectosprevios=insectosprevios+insectos
    print("Después de",contador,"día(s) de recolección, llevas",insectosprevios,"insectos")
    if insectosprevios<30:
      print("Te hace falta recolectar", meta-insectosprevios,"insectos")
    elif insectosprevios>30:
      print("Te has pasado con",insectosprevios-meta,"insectos")
    if insectosprevios>=30:
      print("¡Felicidades, has llegado a la meta!")
      break

def encontrarMayor():
  print("Bienvenido al programa que encuentra al mayor")
  continuar=True
  lista=[]
  while continuar==True:
    numero=int(input("Teclea un número [-1 para salir]: "))
    if numero>-1:  
      lista.append(numero)
      final=max(lista)
    else:
      return(final)

def main():
  menu=True
  while menu==True:
    print(introduccion)
    print(autor)
    print("")
    print("1. Recolectar insectos")
    print("2. Encontrar al mayor")
    print("3. Salir")
    eleccion=int(input("Teclea tu opción"))
    if eleccion==1:
      print("")
      recolectarinsecto()
    elif eleccion==2:
      print("")
      encontrarMayor()
    elif eleccion==3:
      print("Gracias por usar este programa, regresa pronto")
      break
    else:
      print("ERROR. Teclea 1,2 o 3")


main()
