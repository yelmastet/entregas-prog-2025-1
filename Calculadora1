#!/usr/bin/env python3

"""
Título de práctica: breve descripción

Descripción extendida del programa

Autor: ElAutor <el@correo>
Fecha: 2025-02-01
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.


def run():
    """script entrypoint"""

    # **** Poner el código ejecutable de su ejercicio aquí

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
        return "Error: No es posible realizar la división por cero"
    return a / b


def calculadora():
    """Función que solicita al usuario seleccionar una operación
    mediante un menú
    y luego realiza el cálculo."""
    while True:  # Evita que la calculadora se cierre sin avisar.
        # Menú de operaciones.
        print("\nSeleccione la operación que desea realizar: ")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")

        # Bucle para asegurar que se ingrese una opción válida.
        while True:
            operacion = input(
                "Elija la operación que quiere realizar (1/2/3/4): "
            )

            # Verificar si el número ingresado es válido.
            if operacion in ['1', '2', '3', '4']:
                break  # Salir del bucle si el input es correcto.
            else:
                print(
                    "Error: Debe seleccionar una operación válida (1/2/3/4)."
                )

        # Bucle para asegurar que se ingresen caracteres válidos.
        while True:
            try:
                # Ingresar los dos números.
                operando_a = float(input("Ingresa el primer número: "))
                operando_b = float(input("Ingresa el segundo número: "))
                break  # Salir del bucle si todo es correcto.
            except ValueError:
                print("Error: Debe ingresar caracteres válidos.")

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

        # Preguntar si el usuario desea realizar otra operación.
        while True:
            continuar = input("\n¿Desea continuar operando?(si/no):").lower()
            if continuar == 'si':
                break  # Continuar el ciclo y permitir realizar otra operación.
            elif continuar == 'no':
                print("\nGracias por usar la calculadora. ¡Hasta la próxima!")
                return  # Salir de la función y cerrar el programa.
            else:
                print(
                    "Error: Por favor, responde con 'si' o 'no'."
                )  # Si no ingresa 'si' o 'no', pide la respuesta nuevamente.


# Llamar a la calculadora (solo debe ejecutarse cuando se ejecuta este archivo)
if __name__ == "__main__":
    calculadora()


    # **** ****


# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()
