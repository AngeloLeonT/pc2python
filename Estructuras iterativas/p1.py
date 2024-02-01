# Programa para encontrar números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700
# Verifica si el número es divisible por 7 y también es múltiplo de 5
# Imprime el número que cumple con las condiciones
# n = todos los numeros del rango

for n in range(1500, 2701):

    if n % 7 == 0 and n % 5 == 0:

        print(n)

        