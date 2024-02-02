# Función para omitir vocales dentro de una cadena de texto
# Ingresar un texto para después borrar las vocales
# Imprimir el resultado sin las vocales

def omitir_vocales(cadena):
    
    vocales = "aeiouAEIOU"
    resultado = ""
    
    for caracter in cadena:
        if caracter not in vocales:
            resultado += caracter
    
    return resultado

texto = input("Ingrese una cadena de texto: ")

resultado_sin_vocales = omitir_vocales(texto)
print("Texto sin vocales:", resultado_sin_vocales)