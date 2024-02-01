def es_primo(numero):
    """
    Función que verifica si un número es primo.

    Parameters:
    - numero (int): Número a verificar.

    Returns:
    - bool: True si el número es primo, False en caso contrario.
    """
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  # Si es divisible por algún número, no es primo

    return True  # Si no es divisible por ningún número, es primo

# Ejemplo de uso
numero_ingresado = int(input("Ingrese un número para verificar si es primo: "))

# Llama a la función e imprime el resultado
resultado = es_primo(numero_ingresado)
if resultado:
    print(f"{numero_ingresado} es un número primo.")
else:
    print(f"{numero_ingresado} no es un número primo.")