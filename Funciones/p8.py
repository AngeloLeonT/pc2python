def factorial(n):
    """
    Función que calcula el factorial de un número.

    Parameters:
    - n (int): Número entero no negativo.

    Returns:
    - int: Factorial de n.
    """
    if n < 0:
        return "El factorial no está definido para números negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# Ejemplo de uso
numero_ingresado = int(input("Ingrese un número para calcular su factorial: "))

# Llama a la función e imprime el resultado
resultado_factorial = factorial(numero_ingresado)
print(f"El factorial de {numero_ingresado} es {resultado_factorial}.")