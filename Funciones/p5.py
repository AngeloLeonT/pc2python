

def contar(numero, digito):
    """
    Función que cuenta la cantidad de veces que un dígito específico aparece en un número.

    Parameters:
    - numero (int): Número entero en el que se buscará el dígito.
    - digito (int): Dígito que se buscará en el número.

    Returns:
    - int: Cantidad de veces que el dígito aparece en el número.
    """
    # Convierte el número a una cadena para poder utilizar el método count
    numero_str = str(numero)
    
    # Utiliza el método count para contar la cantidad de veces que aparece el dígito
    cantidad = numero_str.count(str(digito))
    
    return cantidad

# Ejemplo de uso
numero_ingresado = int(input("Ingrese un número entero: "))
digito_ingresado = int(input("Ingrese un dígito a buscar: "))

# Llama a la función e imprime el resultado
resultado = contar(numero_ingresado, digito_ingresado)
print(f"El dígito {digito_ingresado} aparece {resultado} veces en el número {numero_ingresado}.")