class ConjuntosDisjuntos:
    def __init__(self, num_nodos):
        self.padre = list(range(num_nodos))
        self.rango = [0] * num_nodos

    def encontrar(self, nodo):
        if self.padre[nodo] != nodo:
            self.padre[nodo] = self.encontrar(self.padre[nodo])
        return self.padre[nodo]

    def unir(self, u, v):
        raiz_u = self.encontrar(u)
        raiz_v = self.encontrar(v)

        if raiz_u != raiz_v:
            if self.rango[raiz_u] < self.rango[raiz_v]:
                self.padre[raiz_u] = raiz_v
            elif self.rango[raiz_u] > self.rango[raiz_v]:
                self.padre[raiz_v] = raiz_u
            else:
                self.padre[raiz_v] = raiz_u
                self.rango[raiz_u] += 1


def kruskal(grafo):
    """
    Implementación del algoritmo de Kruskal.
    
    :param grafo: Lista de aristas en formato (nodo1, nodo2, peso).
    :return: Lista de aristas del árbol de expansión mínima.
    """
    num_nodos = max(max(u, v) for u, v, _ in grafo) + 1
    conjuntos_disjuntos = ConjuntosDisjuntos(num_nodos)
    
    # Ordenar las aristas por peso
    grafo.sort(key=lambda x: x[2])
    
    aem = []
    
    # Iterar sobre las aristas ordenadas
    for u, v, peso in grafo:
        if conjuntos_disjuntos.encontrar(u) != conjuntos_disjuntos.encontrar(v):
            aem.append((u, v, peso))
            conjuntos_disjuntos.unir(u, v)
    
    return aem


# Ejemplo de uso
# Grafo con 5 nodos
grafo = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]

aem = kruskal(grafo)

# Mostrar el árbol de expansión mínima
print("Árbol de expansión mínima:")
for arista in aem:
    print(f"Nodo {arista[0]} - Nodo {arista[1]} con peso {arista[2]}")
