# Función para calcular el factorial de un número teniendo en cuenta que sea un número entero no negativo
# Se obtiene el resultado y se imprime.

def factorial(n):
   
    if n < 0:
        return "El factorial no está definido para números negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

n = int(input("Ingrese un número para calcular su factorial: "))

rfactorial = factorial(n)
print(f"El factorial de {n} es {rfactorial}")