

def omitir_vocales(cadena):
    """
    Función que omite todas las vocales de una cadena de texto.

    Parameters:
    - cadena (str): Cadena de texto ingresada por el usuario.

    Returns:
    - str: Cadena de texto sin vocales.
    """
    vocales = "aeiouAEIOU"
    resultado = ""
    
    for caracter in cadena:
        if caracter not in vocales:
            resultado += caracter
    
    return resultado

# Solicitar al usuario que ingrese una cadena de texto
cadena_ingresada = input("Ingrese una cadena de texto: ")

# Llama a la función e imprime el resultado
resultado_sin_vocales = omitir_vocales(cadena_ingresada)
print("Texto sin vocales:", resultado_sin_vocales)