class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def in_order_traversal(self, nodo):
        if nodo is not None:
            self.in_order_traversal(nodo.izquierda)
            print(nodo.valor, end=' ')
            self.in_order_traversal(nodo.derecha)

    def visualizar_arbol(self, nodo, nivel=0, es_ultimo=True):
        indent = '    ' * (nivel - 1) if nivel > 0 else ''
        connector = '└── ' if es_ultimo else '├── '
        
        if nodo is not None:
            print(f"{indent}{connector}{nodo.valor}")
            hijos = [nodo.izquierda, nodo.derecha]
            for i, hijo in enumerate(hijos):
                es_ultimo_hijo = i == len(hijos) - 1
                self.visualizar_arbol(hijo, nivel + 1, es_ultimo_hijo)

# Ejemplo de uso
arbol = ArbolBinario()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)
arbol.insertar(7)

print("Recorrido en orden (In-order traversal):")
arbol.in_order_traversal(arbol.raiz)
print("\n\nVisualización jerárquica del árbol:")
arbol.visualizar_arbol(arbol.raiz)
