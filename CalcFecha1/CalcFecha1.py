#!/usr/bin/env python3

"""
CalcFecha1: Hacer un programa que haga cálculos de fechas.

Este programa le muestra al usuario
La fecha y hora actual para luego pedirle
que escoja una opción entre días o segundos
para luego hacer el cálculo a fecha y hora futora
si el número ingresado es positivo o a fecha y hora
pasada si el número ingresado es negativo
el programa se podrá usar varias veces ya que
tiene una opción para salir del programa y únicamente
se cerrara al elegir esta.

Autor: David Torres <dstorresr@academia.usbbog.edu.co>

Fecha: 2025-05-28
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.


from datetime import datetime, timedelta


def mostrar_menu():
    """
    Muestra el menú principal de opciones para el usuario.
    """
    print("Escriba 1 para ingresar segundos.")
    print("        2 para ingresar días.")
    print("        3 para salir.")


def obtener_fecha_actual():
    """
    Obtiene la fecha y hora actual del sistema (zona horaria local).

    Returns:
        datetime: La fecha y hora actual.
    """
    return datetime.now()


def pedir_numero(mensaje):
    """
    Solicita al usuario que ingrese un número y valida la entrada.

    Args:
        mensaje (str): Mensaje que se mostrará al usuario.

    Returns:
        float: Número ingresado por el usuario (acepta positivos y negativos).
    """
    while True:
        try:
            entrada = input(mensaje)
            return float(entrada)  # Acepta decimales y negativos
        except ValueError:
            print("Error. intente de nuevo.")


def run():
    """
    Función principal del programa.
    Muestra la fecha actual y permite al usuario
    sumar o restar tiempo en segundos o días.
    Se repite hasta que el usuario elige salir.
    """
    # **** Poner el código ejecutable de su ejercicio aquí

    while True:
        # Obtener y mostrar la fecha actual
        fecha_actual = obtener_fecha_actual()
        print(f"La fecha actual es: {fecha_actual}")

        # Mostrar el menú de opciones
        mostrar_menu()
        opcion = input("< ").strip()

        if opcion == "1":
            # Sumar/restar segundos
            segundos = pedir_numero("Ingrese la cantidad de segundos\n")
            nueva_fecha = fecha_actual + timedelta(seconds=segundos)
            print(f"La nueva fecha es: {nueva_fecha}\n")

        elif opcion == "2":
            # Sumar/restar días
            dias = pedir_numero("Ingrese la cantidad de días\n< ")
            nueva_fecha = fecha_actual + timedelta(days=dias)
            print(f"La nueva fecha es: {nueva_fecha}\n")

        elif opcion == "3":
            # Salir del programa
            print("¡Gracias por usar el programa!")
            break

        else:
            # Opción inválida
            print("Error. Intente de nuevo.\n")

    # **** ****


# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()
