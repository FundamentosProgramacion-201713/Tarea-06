#encoding: UTF-8
#Autor Aaron Villanueva
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
      print("Te hace falta recolectar", total-insectosprevios,"insectos")
    elif insectos previos>30:
      print("Te has pasado con",insectosprevios-total,"insectos")
    if insectosprevios==30:
      print("¡Felicidades, has llegado a la meta!")
def encontrarMayor():
  print("Bienvenido al programa que encuentra al mayor")
  numero=0
  while numero>-1:
    numero=int(input("Teclea un número [-1 para salir]: "))
  final=max(numero)
  return(final)

def main():
  menu=True
  while menu==True:
    print("1. Recolectar insectos")
    print("2. Encontrar al mayor")
    print("3. Salir")
    eleccion=int(input("Teclea tu opción"))
    if eleccion==1:
      recolectarinsecto()
    elif eleccion==2:
      encontrarMayor()
    elif eleccion==3:
      break
    else:
      print("Número no reconocido")


main()
