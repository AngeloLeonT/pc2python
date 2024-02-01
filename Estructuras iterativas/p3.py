numeros_pares = 0
numeros_impares = 0

# Bucle while para el ingreso de números
while True:
    try:
        # Solicitar al usuario que ingrese un número
        numero = int(input("Ingrese un número (o cualquier letra para detenerse): "))
        
        # Verificar si el número es par o impar
        if numero %2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1
    except ValueError:
        # Si se ingresa una letra u otro carácter, salir del bucle
        break

# Mostrar resultados
print(f"\nCantidad de números pares: {numeros_pares}")
print(f"Cantidad de números impares: {numeros_impares}")