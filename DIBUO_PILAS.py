import matplotlib.pyplot as plt
import matplotlib.patches as patches

def dibujar_pila(pila, tope, operacion):
    fig, ax = plt.subplots(figsize=(4, 6))
    max_elementos = 8
    
    # Dibujar estructura de la pila
    for i in range(max_elementos):
        y_pos = (max_elementos - 1 - i) * 0.5  # Posición invertida para apilar hacia arriba
        color = 'lightblue' if i < len(pila) else 'white'
        
        # Dibujar celda
        celda = patches.Rectangle(
            (0.4, y_pos), 0.6, 0.4,
            edgecolor='black', facecolor=color, lw=2
        )
        ax.add_patch(celda)
        
        # Texto del elemento si existe
        if i < len(pila):
            plt.text(0.7, y_pos + 0.2, pila[i], ha='center', va='center', fontsize=12)
    
    # Dibujar puntero TOPE
    flecha_y = (max_elementos - tope) * 0.5 - 0.2
    ax.arrow(0.2, flecha_y, 0.15, 0, 
             head_width=0.1, head_length=0.1, 
             fc='red', ec='red', lw=2)
    
    # Configuración del gráfico
    plt.xlim(0, 1.5)
    plt.ylim(-0.5, 4.5)
    plt.axis('off')
    plt.title(f"{operacion}\nTOPE = {tope}", fontsize=12, pad=20)
    plt.show()

# Simulación de operaciones
pila = []
tope = 0
capacidad = 8

operaciones = [
    ('a', 'X', 'Insertar'),
    ('b', 'Y', 'Insertar'),
    ('c', None, 'Eliminar'),
    ('d', None, 'Eliminar'),
    ('e', None, 'Eliminar'),
    ('f', 'V', 'Insertar'),
    ('g', 'W', 'Insertar'),
    ('h', None, 'Eliminar'),
    ('i', 'R', 'Insertar')
]

# Imprimir pila inicial
print("Pila inicial: []")
print(f"TOPE: {tope}\n")

for i, op in enumerate(operaciones):
    # Aplicar operación
    if op[2] == 'Insertar':
        if tope < capacidad:
            pila.append(op[1])
            tope += 1
    else:
        if tope > 0:
            pila.pop()
            tope -= 1
    
    # Imprimir estado actual
    print(f"Operación {i+1}: {op[0]}. {op[2]} {op[1] if op[1] else ''}".strip())
    print(f"Pila: {pila}")
    print(f"TOPE: {tope}\n")
    
    # Dibujar estado actual
    dibujar_pila(pila.copy(), tope, f"{op[0]}. {op[2]} {op[1] if op[1] else ''}".strip())
