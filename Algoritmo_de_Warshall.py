def warshall(grafo):
    """
    Implementación del algoritmo de Warshall.
    
    :param grafo: Matriz de adyacencia del grafo, donde grafo[i][j] es 1 si hay arista de i a j, y 0 de lo contrario.
    :return: Matriz de alcanzabilidad, donde alcanzabilidad[i][j] es 1 si hay camino de i a j.
    """
    num_nodos = len(grafo)
    
    # Copiar la matriz original para no modificarla
    alcanzabilidad = [[grafo[i][j] for j in range(num_nodos)] for i in range(num_nodos)]
    
    # Algoritmo de Warshall
    for k in range(num_nodos):
        for i in range(num_nodos):
            for j in range(num_nodos):
                # Si hay camino de i a k y de k a j, entonces hay camino de i a j
                alcanzabilidad[i][j] = alcanzabilidad[i][j] or (alcanzabilidad[i][k] and alcanzabilidad[k][j])
    
    return alcanzabilidad

# Ejemplo de uso
# Grafo con 5 nodos
grafo = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

matriz_alcanzabilidad = warshall(grafo)

# Mostrar la matriz de alcanzabilidad
for i in range(len(matriz_alcanzabilidad)):
    print(f"Alcanzabilidad desde el nodo {i}: {matriz_alcanzabilidad[i]}")
