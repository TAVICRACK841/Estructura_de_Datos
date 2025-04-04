import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, u, v, peso):
        if u not in self.grafo:
            self.grafo[u] = []
        self.grafo[u].append((v, peso))

    def dijkstra(self, inicio):
        monticulo = [(0, inicio)]
        distancias = {vertice: float('inf') for vertice in self.grafo}
        distancias[inicio] = 0

        while monticulo:
            distancia_actual, vertice_actual = heapq.heappop(monticulo)

            if distancia_actual > distancias[vertice_actual]:
                continue

            for vecino, peso in self.grafo.get(vertice_actual, []):
                distancia = distancia_actual + peso
                
                # Modificación clave: usar get con valor por defecto
                if distancia < distancias.get(vecino, float('inf')):
                    distancias[vecino] = distancia
                    heapq.heappush(monticulo, (distancia, vecino))

        return distancias

# Ejemplo de uso
g = Grafo()
g.agregar_arista('A', 'B', 1)
g.agregar_arista('A', 'C', 4)
g.agregar_arista('B', 'C', 2)
g.agregar_arista('B', 'D', 5)
g.agregar_arista('C', 'D', 1)
g.agregar_arista('D', 'E', 3)
g.agregar_arista('C', 'E', 2)

print(g.dijkstra('A'))  # Salida: {'A': 0, 'B': 1, 'C': 3, 'D': 4, 'E': 5}
