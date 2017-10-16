#encoding: UTF-8
#Autor Aaron Villanueva
def recolectarinsecto():
  
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
