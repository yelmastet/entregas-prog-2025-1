#!/usr/bin/env python3

"""
Texto1: Hacer un programa que haga cambios en un texto introducido.

Este programa le pide al usuario
ingresar una línea de texto para luego
mostrar una lista donde se puede escoger
Entre diferentes acciónes de transformación
del texto (pasar a minúsculas, pasar a mayúsculas,
invertir mayúsculas y minúsculas, pasar a capitalización,
pasar a titulación, reemplazar espacios por guiones bajos
y salir del programa) guardando el texto sin que sea
modificable para permitir hacer varias transformaciones
del mismo texto sin necesidad de cerrar el programa.

Autor: David Torres <dstorresr@academia.usbbog.edu.co>

Fecha: 2025-05-05
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.


def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    """
    print("\nSeleccione la transformación que desea realizar:")
    print(" 1. Pasar a minúsculas.")
    print(" 2. Pasar a mayúsculas.")
    print(" 3. Invertir mayúsculas y minúsculas.")
    print(" 4. Pasar a capitalización.")
    print(" 5. Pasar a titulación.")
    print(" 6. Reemplazar espacios por guiones bajos.")
    print(" 7. Salir.")


def aplicar_transformacion(texto, opcion):
    """
    Aplica la transformación seleccionada al texto.

    Args:
        texto (str): El texto original.
        opcion (int): La opción seleccionada del menú.

    Returns:
        str: El texto transformado.
    """
    if opcion == 1:
        return texto.lower()
    elif opcion == 2:
        return texto.upper()
    elif opcion == 3:
        return texto.swapcase()
    elif opcion == 4:
        return texto.capitalize()
    elif opcion == 5:
        return texto.title()
    elif opcion == 6:
        return texto.replace(' ', '_')
    else:
        return texto  # Por si llega una opción inválida


def run():
    """
    Función principal que gestiona la entrada del usuario y el ciclo del menú.
    """
    # **** Poner el código ejecutable de su ejercicio aquí

    # Validar que el usuario no deje la entrada vacía
    while True:
        texto_original = input("> Ingrese la línea de texto:\n< ")
        if texto_original.strip() == "":
            print("> El texto no puede estar vacío. Intente de nuevo.")
        else:
            break

    while True:
        mostrar_menu()
        try:
            opcion = int(input("< "))
        except ValueError:
            print("> Por favor, ingrese un número del 1 al 7.")
            continue

        if opcion == 7:
            print("> Gracias!")
            break
        elif 1 <= opcion <= 6:
            resultado = aplicar_transformacion(texto_original, opcion)
            print(f"> Resultado: {resultado}")
        else:
            print("> Opción inválida. Intente de nuevo.")
    # **** ****


# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()
