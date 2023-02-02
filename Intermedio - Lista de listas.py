# Crea una funcion que dada una lista, que puede o no contener otras listas en su interior, retorne una lista unica con los 
# elementos contenidos dentro de cada una de las listas de su interior.

def lista_principal(lista):
    if type(lista) != list:
        return None
    
    resultado = []
    cola = [lista]

    while cola:
        elemento = cola.pop(0)
        if type(elemento) == list:
            cola.extend(elemento)
        else:
            resultado.append(elemento)

    return resultado

print(lista_principal([1, 2, 3, [1, 2, 3,[1, 2, 3]]]))
