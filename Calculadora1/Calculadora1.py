#!/usr/bin/env python3

"""
Calculadora1: Hacer un programa de calculadora sencilla.

1. Pregunte al usuario por dos operandos
(puede llamarlo operando A y operando B).
2. Después de tener los operandos,
preguntar por cuál operación realizar.
Sólo debe realizar una operación.
3. Implemente las cuatro operaciones aritméticas básicas:
Suma, Resta, Multiplicación y División.
4. El menú de operaciones puede ser numérico o de texto.
5. Muestre en pantalla el resultado de la operación.

Autor: David Torres <dstorresr@academia.usbbog.edu.co>
Fecha: 2025-03-02
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.


def sumar(a, b):
    """
    Función que suma dos números.
    a (float) = El primer número.
    b (float) = El segundo número.

    Returns:
        float: Resultado de la suma de a y b.
    """
    return a + b


def restar(a, b):
    """
    Función que resta dos números.
    a (float) = El primer número.
    b (float) = El segundo número.

    Returns:
        float: Resultado de la resta de a y b.
    """
    return a - b


def multiplicar(a, b):
    """
    Función que multiplica dos números.
    a (float) = El primer número.
    b (float) = El segundo número.

    Returns:
        float: Resultado de la multiplicación de a y b.
    """
    return a * b


def dividir(a, b):
    """
    Función que divide dos números.
    Si el divisor es 0, devuelve un mensaje de error.
    a (float) = El primer número.
    b (float) = El segundo número.

    Returns:
        float or str: Resultado de la división o mensaje de error si b es 0.
    """
    if b == 0:
        return "Error: No es posible realizar la división por cero"
    return a / b


def run():
    """Función que solicita al usuario seleccionar una operación
    mediante un menú para luego realizar el cálculo."""
    """script entrypoint"""

    # **** Poner el código ejecutable de su ejercicio aquí

    # Ingresar los dos Operandos.
    operando_a = float(input("Ingresa el operando A: "))
    operando_b = float(input("Ingresa el operando B: "))

    # Mostrar el menú de operaciones.
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    operacion = input("Elija la operación que quiere realizar (1/2/3/4): ")

    # Realizar la operación seleccionada.
    if operacion == '1':
        print(
            f"Se hizo una suma: {operando_a} + {operando_b} = "
            f"{sumar(operando_a, operando_b)}"
        )
    elif operacion == '2':
        print(
            f"Se hizo una resta: {operando_a} - {operando_b} = "
            f"{restar(operando_a, operando_b)}"
        )
    elif operacion == '3':
        print(
            f"Se hizo una multiplicación: {operando_a} * {operando_b} = "
            f"{multiplicar(operando_a, operando_b)}"
        )
    elif operacion == '4':
        print(
            f"Se hizo una división: {operando_a} / {operando_b} = "
            f"{dividir(operando_a, operando_b)}"
        )
    else:
        print("Operación no válida. Inténtelo de nuevo.")

    # **** ****


# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()
