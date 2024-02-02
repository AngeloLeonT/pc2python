# Se crea una función de contar la cantidad de veces que aparece un dígito en un número
# Se convierte el número a una cadena para poder utilizar el método count
# Se introduce la cantidad de números

def contar(numero, digito):

    n_str = str(numero)
    
    cantidad = n_str.count(str(digito))
    
    return cantidad

numero_ingresado = int(input("Ingrese un número entero: "))
digito_ingresado = int(input("Ingrese un dígito a buscar: "))

resultado = contar(numero_ingresado, digito_ingresado)
print(f"El dígito {digito_ingresado} aparece {resultado} veces en el número {numero_ingresado}.")