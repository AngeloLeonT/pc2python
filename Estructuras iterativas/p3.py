# Bucle while para el ingreso de números
# Solicitar al usuario que ingrese un número
# Verificar si el número es par o impar
# Si se ingresa una letra u otro carácter, salir del bucle
# Mostrar resultados


pares = 0
impares = 0

while True:
    try:
        n = int(input("Ingrese un número (o cualquier letra para detenerse): "))
        
        if n %2 == 0:
            pares += 1
        else:
            impares += 1
    except ValueError:
        break

print(f"\nCantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")