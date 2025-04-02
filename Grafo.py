import networkx as nx
import matplotlib.pyplot as plt

# Función para ingresar los estados y sus conexiones
def input_states_and_connections():
    states = []
    connections = []

    print("Ingrese el nombre de los 7 Estados de la República Mexicana:")
    for i in range(7):
        state = input(f"Estado {i+1}: ")
        states.append(state)

    print("Ingrese las conexiones entre los Estados y sus costos de traslado:")
    print("Formato: Estado1 Estado2 Costo")
    while True:
        connection = input("Conexión (o presione Enter para terminar): ")
        if connection == "":
            break
        connection_data = connection.split()
        if len(connection_data) == 3:
            connections.append((connection_data[0], connection_data[1], float(connection_data[2])))
        else:
            print("Formato inválido. Intente nuevamente.")

    return states, connections

# Función para recorrer sin repetición
def traverse_without_repetition(states, connections):
    G = nx.Graph()
    for connection in connections:
        G.add_edge(connection[0], connection[1], weight=connection[2])

    path = list(nx.dfs_preorder_nodes(G, source=states[0]))
    total_cost = sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))

    return path, total_cost

# Función para recorrer con repetición
def traverse_with_repetition(states, connections):
    G = nx.Graph()
    for connection in connections:
        G.add_edge(connection[0], connection[1], weight=connection[2])

    path = list(nx.dfs_preorder_nodes(G, source=states[0]))
    path.append(states[0])  # Regresar al inicio para repetir
    total_cost = sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))

    return path, total_cost

# Función para dibujar los grafos
def draw_graph(states, connections, path_a, path_b):
    G = nx.Graph()
    for connection in connections:
        G.add_edge(connection[0], connection[1], weight=connection[2])

    pos = nx.spring_layout(G)

    # Grafo del recorrido sin repetición
    plt.figure(figsize=(10, 5))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
    nx.draw_networkx_edges(G, pos, edgelist=[(path_a[i], path_a[i+1]) for i in range(len(path_a)-1)], edge_color='blue', width=2)
    plt.title("Recorrido sin repetición")
    plt.show()

    # Grafo del recorrido con repetición
    plt.figure(figsize=(10, 5))
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='gray', node_size=2000, font_size=10)
    nx.draw_networkx_edges(G, pos, edgelist=[(path_b[i], path_b[i+1]) for i in range(len(path_b)-1)], edge_color='red', width=2)
    plt.title("Recorrido con repetición")
    plt.show()

# Programa principal
states, connections = input_states_and_connections()

# Recorrido sin repetición
path_a, cost_a = traverse_without_repetition(states, connections)
print("\nRecorrido sin repetición:", path_a)
print("Costo total sin repetición:", cost_a)

# Recorrido con repetición
path_b, cost_b = traverse_with_repetition(states, connections)
print("\nRecorrido con repetición:", path_b)
print("Costo total con repetición:", cost_b)

# Dibujar grafos
draw_graph(states, connections, path_a, path_b)
