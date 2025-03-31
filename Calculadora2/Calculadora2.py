#!/usr/bin/env python3

"""
Calculadora2: Hacer un programa de calculadora avanzada.

Esta calculadora le pregunta al usuario
por la operación que desee realizar
(suma,resta,multiplicación, división, potenciación, división entera o módulo).
Al seleccionar la operación deseada le solicitará dos operandos
que al momento de ser brindados el programa
los opera y muestra el resultado en pantalla
teniendo en cuenta la operación elegida.

Autor: David Torres <dstorresr@academia.usbbog.edu.co>

Fecha: 2025-03-31
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.


def sumar(a, b):
    """
    Suma dos números.
    a (float) = El primer número.
    b (float) = El segundo número.

    Returns:
        float: Resultado de la suma de a y b.
    """
    return a + b


def restar(a, b):
    """
    Resta dos números.
    a (float) = El primer número.
    b (float) = El segundo número.

    Returns:
        float: Resultado de la resta de a y b.
    """
    return a - b


def multiplicar(a, b):
    """
    Multiplica dos números.
    a (float) = El primer número.
    b (float) = El segundo número.

    Returns:
        float: Resultado de la multiplicación de a y b.
    """
    return a * b


def dividir(a, b):
    """
    Divide dos números. Si el divisor es 0, devuelve un mensaje de error.
    a (float) = El primer número.
    b (float) = El segundo número.

    Returns:
        float or str: Resultado de la división o mensaje de error si b es 0.
    """
    if b == 0:
        return "No se puede dividir por cero, intente nuevamente"
    return a / b


def potenciar(a, b):
    """
    Resuelve la potenciación de un número.
    a (float) = El primer número.
    b (float) = El segundo número.

    Returns:
        float: Resultado de la potencia de a y b.
    """
    return a ** b


def diventera(a, b):
    """
    División entera de dos números dando un resultado sin decimales.
    Si el divisor es 0, devuelve un mensaje de error.
    a (float) = El primer número.
    b (float) = El segundo número.

    Returns:
        int or str: Resultado división entera o mensaje de error si b es 0.
    """
    if b == 0:
        return "No se puede dividir por cero, intente nuevamente."
    return int(a // b)  # El resultado será un número entero.


def modulo(a, b):
    """
    Calcula el residuo de la división entre dos números.
    a (float) = El primer número.
    b (float) = El segundo número.

    Returns:
        float: Resultado del módulo de a y b.
    """
    return int(a % b)  # El resultado será un número entero.


def run():
    """
    Función que solicita al usuario seleccionar una operación
    mediante un menú y luego realiza el cálculo.
    """

    # **** Poner el código ejecutable de su ejercicio aquí

    while True:  # Evita que la calculadora se cierre sin avisar.
        # Menú de operaciones.
        print("\nSeleccione la operación que desea realizar: ")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potenciación")
        print("6. División entera")
        print("7. Módulo")
        print("8. Salir de la calculadora")

        # Bucle para asegurar que se ingrese una opción válida.
        while True:
            operacion = input(
                "Elija la operación que quiere realizar (1/2/3/4/5/6/7/8): "
            )
            if operacion in ['1', '2', '3', '4', '5', '6', '7', '8']:
                break
            print("\nSeleccione una operación válida, intente nuevamente.")
        if operacion == '8':
            print("\nGracias por usar la calculadora. ¡Hasta la próxima!")
            break  # Salir de la función y cerrar el programa.

        # Bucle para asegurar que se ingresen caracteres válidos.
        while True:
            operando_a = input(
                "Ingresa el primer operando (Vacío para cancelar): "
                )
            if operando_a == "":  # Salir de la calculadora si está vacío.
                print("\nGracias por usar la calculadora. ¡Hasta la próxima!")
                return
            operando_b = input(
                "Ingresa el segundo número (Vacío para cancelar): "
                )
            if operando_b == "":  # Salir de la calculadora si está vacío.
                print("\nGracias por usar la calculadora. ¡Hasta la próxima!")
                return
            try:  # Verifica que el operando ingresado sea un float.
                operando_a = float(operando_a)
                operando_b = float(operando_b)
                break
            except ValueError:
                print(
                    "\nDebe ingresar caracteres válidos, intente nuevamente."
                    )

        # Realiza la operación seleccionada.
        if operacion == '1':
            print(
                f"Resultado: {sumar(operando_a, operando_b)}"
                )
        elif operacion == '2':
            print(
                f"Resultado: {restar(operando_a, operando_b)}"
                )
        elif operacion == '3':
            print(
                f"Resultado: {multiplicar(operando_a, operando_b)}"
                )
        elif operacion == '4':
            print(
                f"Resultado: {dividir(operando_a, operando_b)}"
                )
        elif operacion == '5':
            print(
                f"Resultado: {potenciar(operando_a, operando_b)}"
                )
        elif operacion == '6':
            print(
                f"Resultado: {diventera(operando_a, operando_b)}"
                )
        elif operacion == '7':
            print(
                f"Resultado: {modulo(operando_a, operando_b)}"
                )

        # Preguntar si el usuario desea realizar otra operación.
        while True:
            continuar = input("\n¿Desea continuar operando? (si/no): ").lower()
            if continuar in ['si', 'no']:
                break
            print("\nError: Por favor, responde con 'si' o 'no'.")
        if continuar == 'no':
            print("\nGracias por usar la calculadora. ¡Hasta la próxima!")
            return
    # **** ****


# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()
