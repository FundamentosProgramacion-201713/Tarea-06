# ecnoding: UTF-8
# Autor: LuisMiguel Baqueiro
# Matricula: 1745997
# Programa para recolectar insectos
print("Bienvenido al programa que registra los insectos que recolectas")
insectos = 0
dias = 0
while insectos < 30:
    insectos += int(input("¿Cuántos insectos atrapaste hoy? "))
    dias += 1
    print("Después de %s día(s) denrecolección, llevas %s insectos" % (dias, insectos))
    falta = 30 - insectos
    if insectos <= 30:
        print("Te hace falta recolectar %s insectos" % falta)
    else:
        print("Te has pasado con %s insectos" % (falta + (falta * -2)))
    if insectos >= 30:
        print("¡Felicidades, has llegado a la meta!")
        print("")