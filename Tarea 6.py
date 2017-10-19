#encoding: UTF-8
#Autor: Eduardo Roberto Müller Romero, A01745219

def insectos():
	pasado = 0
	total = 0
	dia_pasado = 0
	while total < 30:
		dia = int(input("¿Cuantos insectos capturaste hoy? "))
		total = dia + pasado
		dias = dia_pasado + 1
		print("En", dias, "día(s) has capturado", total, "insectos")
		pasado = total
		dia_pasado = dias
	print("felicidades, llegaste a la meta")
	diferencia = total - 30
	if diferencia > 0:
		print("Te pasaste por", diferencia, "insectos")

def mayorvalor():
	valor = 0
	a = []
	while valor != -1:
		valor = int(input("Teclea un valor (teclea -1 para salir) "))
		a.append(valor)
	mayor = max(a)
	print(mayor, "es el mayor numero ingresado")

def main():
	opcion = 5
	while opcion != 3:
		print("Programas")
		print("1. Contador de insectos (llegar a 30)")
		print("2. Encontrar el mayor valor en la lista que escribas")
		print("Escribe 3 para salir")
		opcion = int(input("¿Qué deseas hacer hoy? "))
		if opcion == 1:
			print("Bienvenido al contador de insectos")
			insectos()
		elif opcion == 2:
			print("Escribe datos en una lista y encuentra el mayor de ellos")
			mayorvalor()
	print("Gracias por usar el programa, vuelve pronto y ponle 100 ;)")

main()