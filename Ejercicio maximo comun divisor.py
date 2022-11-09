# Crea un programa capaz de encontrar el maximo comun divisor entre dos numeros dados.

def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a%b)

print(mcd(120, 116))


def mcd_alt(x, y):
    if x > y:
        menor = y
    else:
        menor = x
    for i in range(1, menor + 1):
        if x % i == 0 and y % i == 0:
            mcd = i
    return mcd

print(mcd_alt(120, 116))


def mcd_euclides(x, y):
    while y:
        x, y = y, x%y
    return x

print(mcd_euclides(120, 116))