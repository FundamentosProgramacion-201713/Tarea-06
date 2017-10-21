#UTF-8
#Natalia Meraz Tostado
#Crear un proyecto que te diga cuantos insectos te faltan

def contarInsectos():
    insectos = int(input("¿Cuántos insectos atrapaste hoy?: "))
    total = insectos
    while total <= 30 or total >= 30:

        for x in range(1,5,1):
            faltantes = 30 - total
            print("Después de", x, "dia(s) de recolección, llevas", total, "insectos")

            if faltantes < 30 and faltantes > 0:
                print("Te hace falta recolectar", faltantes, "insectos")
                nuevos = int(input("¿Cuántos insectos atrapaste hoy?: "))
                total = total + nuevos
            elif faltantes == 0:
                print("¡Felicidades, has llegado a la meta!")
            elif total > 30:
                print("Te has pasasdo con", (faltantes*-1), "insectos")
                print("¡Felicidades, has llegado a la meta!")
        break
def main():
    print("Bienvenido al programa que registra los insectos que recolectas")
    contarInsectos()

main()