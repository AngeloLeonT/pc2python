# Función para generar la serie de Fibonacci hasta un límite
def fibonacci(limite):
    fibonacci_series = [0, 1]
    while fibonacci_series[-1] + fibonacci_series[-2] <= limite:
        siguiente_numero = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(siguiente_numero)
    return fibonacci_series

# Límite para la serie de Fibonacci (50 en este caso)
limite = 50

# Llama a la función y obtén la serie de Fibonacci
serie_fibonacci = fibonacci(limite)

# Imprime la serie de Fibonacci
print("Serie de Fibonacci hasta", limite, ":", serie_fibonacci)