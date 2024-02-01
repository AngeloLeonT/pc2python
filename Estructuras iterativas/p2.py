
h = 5

# Imprime la primera mitad del patrón
for i in range(1, h + 1):
    for j in range(i):
        print('*', end=' ')
    print()

# Imprime la segunda mitad del patrón
for i in range(h - 1, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()
