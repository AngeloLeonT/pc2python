# Función para generar la serie de Fibonacci hasta un límite (50)
# Llama a la función y obtén la serie de Fibonacci
# Imprime la serie de Fibonacci

def fibonacci(limite):
    fibonacci = [0, 1]
    while fibonacci[-1] + fibonacci[-2] <= limite:
        siguiente_numero = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(siguiente_numero)
    return fibonacci

limite = 50

serie_fibonacci = fibonacci(limite)

print("Serie de Fibonacci hasta", limite, ":", serie_fibonacci)