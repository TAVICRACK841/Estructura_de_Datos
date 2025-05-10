def merge(left, right):
    resultado = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1
    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado

def mezcla_directa(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    left = mezcla_directa(lista[:mid])
    right = mezcla_directa(lista[mid:])
    return merge(left, right)

# Lista desordenada
lista = [38, 27, 43, 3, 9, 82, 10]

# Ordenar con mezcla directa
lista_ordenada = mezcla_directa(lista)
print("Lista ordenada con mezcla directa:", lista_ordenada)
