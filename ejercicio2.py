# ecnoding: UTF-8
# Autor: LuisMiguel Baqueiro
# Matricula: 1745997
# Funcion para saber el mayor número
print("Bienvenido al programa que encuentra el mayor")
lista = []
dato = int(input("Valor [-1 para salir]: "))
while dato != -1:
    lista.append(dato)
    dato = int(input("Valor [-1 para salir]: "))
if dato == -1 and len(lista) == 0:
    print("No hay valor mayor")
    print("")
else:
    print("El mayor es: ", max(lista))