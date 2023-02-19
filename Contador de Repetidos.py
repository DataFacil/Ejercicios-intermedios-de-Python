# Dada una lista de elementos, crea una función que retorne una lista de tuplas, donde cada tupla contenga 
# en su primer elemento, un valor de la lista, y en su segundo elemento, la cantidad de veces que
# aparece ese valor en la lista original.

def lista_de_tuplas(lista):
    if type(lista) != list:
        return None
    
    else:
        contador = {}
        for elem in lista:
            if elem in contador:
                contador[elem] += 1
            else:
                contador[elem] = 1
        
        respuesta = list(contador.items())
        return respuesta
    

print(lista_de_tuplas(['data', 'data', 'data', 'facil', 'facil', 1, 2, 3, 4, 5, 5, 5]))