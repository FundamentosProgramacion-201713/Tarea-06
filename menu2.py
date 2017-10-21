#encoding: UTF-8
#Autor: jose Antonio Vazquez Gabian

def juntarinsecto():
   print("Bienvenido al programa que registra los insectos que recolectas")
   contador=0
   bichos=0
   meta=30
   activo=True
   while activo==True:
     insectos=int(input("¿Cuántos insectos atrapaste hoy? " ))
     contador+=1
     bichos=bichos+insectos
     print("Después de",contador,"día(s) de recolección, llevas",bichos,"insectos")
     if bichos<30:
       print("Te hace falta recolectar", meta-bichos,"insectos")
     elif bichos>30:
       print("Te has pasado con",bichos-meta,"insectos")
     if bichos>=30:
       print("¡Felicidades, has llegado a la meta!")
       print("")
       break

def hallarmayor():
   print("Bienvenido al programa que encuentra el mayor")
   lista=[]
   mayor = int(input("Teclea un número [-1 para salir]: "))
   while mayor != -1:
       lista.append(mayor)
       mayor = int(input("Teclea un número [-1 para salir]: "))
   if mayor == -1 and len(lista) == 0:
       lista.append(mayor)
       print("No hay valor mayor")
       print("")
   else:
       print("El mayor es: ", max(lista))

def main():
   menu=True
   while menu==True:
     print("Tarea 06. Ciclos While")
     print("Autor : Jose Antonio Vazquez Gabian")
     print("")
     print("1. Recolectar insectos")
     print("2. Encontrar el mayor")
     print("3. Salir")
     opcion=int(input("Teclea tu opción: "))
     if opcion==1:
       print("")
       juntarinsecto()
     elif opcion==2:
       print("")
       mayorfinal=hallarmayor()
       print("El mayor es:", mayorfinal)
       print("")
     elif opcion==3:
       print("Gracias por usar este programa, regresa pronto.")
       break
     else:
         print("ERROR. Teclea 1,2 o 3")

main()