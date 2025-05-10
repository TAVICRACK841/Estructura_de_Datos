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


def detectar_secuencias(lista):
    secuencias = []
    inicio = 0
    for i in range(1, len(lista)):
        if lista[i] < lista[i - 1]:
            secuencias.append(lista[inicio:i])
            inicio = i
    secuencias.append(lista[inicio:])
    return secuencias

def mezcla_equilibrada(lista):
    secuencias = detectar_secuencias(lista)
    while len(secuencias) > 1:
        nuevas_secuencias = []
        for i in range(0, len(secuencias), 2):
            if i + 1 < len(secuencias):
                fusion = intercalar(secuencias[i], secuencias[i+1])
                nuevas_secuencias.append(fusion)
            else:
                nuevas_secuencias.append(secuencias[i])
        secuencias = nuevas_secuencias
    return secuencias[0]

# Lista con secuencias parcialmente ordenadas
lista = [1, 3, 5, 2, 4, 6, 0, 7, 8]

# Ordenar con mezcla equilibrada
lista_ordenada = mezcla_equilibrada(lista)
print("Lista ordenada con mezcla equilibrada:", lista_ordenada)
