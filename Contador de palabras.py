# Crea un programa que reciba una frase, y devuelva un diccionario con la cantidad de veces
# que se repite cada palabra en esa frase.

def dic_contador():
    parrafo = input('Escribe tu frase ')

    contador = {}
    palabras = parrafo.replace(',', '').replace('.', '').lower().split()

    for elem in palabras:
        if elem in contador:
            contador[elem] += 1
        else:
            contador[elem] = 1

    return(contador)
    
print(dic_contador())