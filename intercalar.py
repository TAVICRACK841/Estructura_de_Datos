def intercalar(lista1, lista2):
    resultado = []
    i, j = 0, 0
    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    # Agregar los elementos restantes
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado

# Listas ordenadas de ejemplo
lista_a = [1, 3, 5, 7]
lista_b = [2, 4, 6, 8]

# Uso de la función
lista_intercalada = intercalar(lista_a, lista_b)
print("Lista intercalada:", lista_intercalada)
