def floyd_warshall(grafo):
    """
    Implementación del algoritmo de Floyd-Warshall.
    
    :param grafo: Matriz de adyacencia del grafo, donde grafo[i][j] es el peso de la arista entre i y j.
                  Si no hay arista directa, el valor es float('inf').
    :return: Matriz de distancias mínimas entre todos los pares de nodos.
    """
    num_nodos = len(grafo)
    
    # Copiar la matriz original para no modificarla
    distancias = [[float('inf')] * num_nodos for _ in range(num_nodos)]
    
    # Inicializar la matriz de distancias con los valores del grafo
    for i in range(num_nodos):
        for j in range(num_nodos):
            distancias[i][j] = grafo[i][j]
            if i == j:  # Distancia a sí mismo es 0
                distancias[i][j] = 0
    
    # Algoritmo de Floyd-Warshall
    for k in range(num_nodos):
        for i in range(num_nodos):
            for j in range(num_nodos):
                # Si el camino a través del nodo k es más corto, actualizar la distancia
                distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])
    
    return distancias

# Ejemplo de uso
# Grafo con 5 nodos
grafo = [
    [0, 3, float('inf'), 7, float('inf')],
    [8, 0, 2, float('inf'), 4],
    [5, float('inf'), 0, 1, 7],
    [2, float('inf'), float('inf'), 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), 6, 0]
]

distancias_minimas = floyd_warshall(grafo)

# Mostrar las distancias mínimas
for i in range(len(distancias_minimas)):
    print(f"Distancias desde el nodo {i}: {distancias_minimas[i]}")
