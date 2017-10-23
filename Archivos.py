# encoding:UTF-8
# Autor: Carlos Pano Hernández
# Tarea 06. Ciclos while


# Descripción: Este progrma resuelve múltiples ejercicios como un contador de insectos y contador del mayor número en una lista.

def contarInsectos():
    print("")
    print("Bienvenido al programa que registra los insectos que recolectas")
    print("")

    insectos = 0  # Incio del counter de insectos.
    dias = 0  # Inicio de counter de días.
    restantes = 30  # Operador para insectos faltantes.

    while insectos < 30:
        cantidad = int(input("¿Cuántos insectos atrapaste hoy?"))  # Pregunta isnectos
        dias = dias + 1
        insectos = insectos + cantidad

        if insectos > 30:  # Si llega a MÁS DE 30
            print("Después de", dias, "día(s) de recolección, llevas:", insectos, "insectos.")
            print("Te pasaste por", insectos - 30, "insectos")  # Restante de insectos
            print("")
            print("¡Felicidades, has llegado a la meta!")
            print("")
            break

        if insectos == 30:  # Si llega a 30
            print("Después de", dias, "día(s) de recolección, llevas:", insectos, "insectos.")
            print("Te has pasado con", insectos - 30, "insectos.")  # Si se pasa, da el número de insectos excedentes.
            print("")
            print("¡Felicidades, has llegado a la meta!")
            print("")
            break

        print("Después de", dias, "día(s) de recolección, llevas:", insectos,
              "insectos.")  # Agrega los insectos y los fuciona al print.
        print("")
        print("Te hace falta recolectar", restantes - insectos, "insectos")  # Restante de insectos


def escogerMayor():
    print("")
    print("Bienvenido al programa que encuentra el mayor")

    elementoInicial = 0  # Elemento inicial de la lista.
    mayor = [elementoInicial]  # Primer elemento

    elementoNuevo = int(input("Teclea un número [-1 para salir]:"))  # Input del usuario
    mayor.append(elementoNuevo)
    while elementoNuevo != -1:
        elementoNuevo = int(input("Teclea un número [-1 para salir]:"))  # Input del usuario
        mayor.append(
            elementoNuevo)  # Eppend es un comando que agrega elementos a una lista en la última posición. Fué comprendido en la página: http://es.diveintopython.net/odbchelper_list.html
        # Agrega nuevo elemento a la lista y repite el siclo si:

    # Esto no se cumple.
    if elementoNuevo == -1:
        print("")
        print("El mayor es:",
              (max(mayor)))  # (Max(lista)) sacado de Internet: https://www.youtube.com/watch?v=Qd6Sjg0Jz1I
        print("")


def main():
    seleccion = 0

    while seleccion >= 0:  # Inicio de while. NOTA: SE DEBE ENTENDER EL USO DE TRUE Y FALSE PARA FUTURAS TAREAS.
        print("""Tarea 06. Ciclos While
Autor: Carlos Pano Hernández
        
        1. Recolectar insectos
        2. Encontrar el mayor
        3. Salir
        """)

        seleccion = int(input("Teclea tu opción:"))

        if seleccion == 1:
            contarInsectos()

        elif seleccion == 2:
            escogerMayor()

        elif seleccion == 3:
            print("")
            print("Gracias por usar este programa, regresa pronto.")
            break

        else:  # Cualquier número lo marca con error.
            print("")
            print("ERROR, teclea 1,2,3")
            print("")


main()
