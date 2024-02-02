# Función para verificar si el número es primo o no.
# Los números menores o iguales a 1 no son primos
# Si es divisible por algún número, no es primo
# Imprimir el resultado

def es_primo(numero):
   
    if numero <= 1:
        return False 

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  

    return True  

numero = int(input("Ingrese un número para verificar si es primo: "))

resultado = es_primo(numero)
if resultado:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")