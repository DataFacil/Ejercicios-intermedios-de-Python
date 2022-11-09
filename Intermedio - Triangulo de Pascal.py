# Construye el Triángulo de Pascal, que funcione con cualquier cantidad de filas
from math import factorial


filas = int(input('Ingrese el numero de filas '))

# loop principal
for n in range(filas + 1):
    # loop de espaciado
    for j in range(filas - n + 1):
        print(end = ' ')
    # loop para imprimir el numero
    for r in range(n + 1):
        numero = factorial(n) / (factorial(n - r) * factorial(r))
        print(int(numero), end = ' ')

    # salto de linea
    print()