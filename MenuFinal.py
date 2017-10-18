#encoding: UTF-8
#Autor Aaron Villanueva

#Esta función registra el número de insectos recolectados e imprime el número restante para obtener 30. La función usa un contador para los insectos.
#Si la meta se alcanza se informa al usuario. Si la meta se rebasa, se indica cuantos insectos adicionales se recolectaron. 
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
      print("")
      break

#Esta función captura una serie de números introducidos por el usuario y los agrega a una lista.
#Posteriomente, regresa el valor más alto de la lista.
def encontrarMayor():
  print("Bienvenido al programa que encuentra al mayor")
  continuar=True
  lista=[]
  while continuar==True:
    numero=int(input("Teclea un número [-1 para salir]: "))
    if numero>-1:  
      lista.append(numero)
      final=max(lista)
    elif numero==-1:
      return(final)

def main():
  menu=True
  while menu==True:
    print("Tarea 06. Ciclos While")
    print("Autor Aaron Villanueva")
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
      mayorfinal=encontrarMayor()
      print(mayorfinal)
      print("")
    elif eleccion==3:
      print("Gracias por usar este programa, regresa pronto")
      break
    else:
      print("ERROR. Teclea 1,2 o 3")

main()
