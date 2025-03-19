class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ColaEnlazada:
    def __init__(self, nombre):
        self.nombre = nombre
        self.frente = None
        self.final = None

    def is_empty(self):
        return self.frente is None

    def enqueue(self, valor):
        nodo = Nodo(valor)
        if self.is_empty():
            self.frente = nodo
            self.final = nodo
        else:
            self.final.siguiente = nodo
            self.final = nodo

    def dequeue(self):
        if self.is_empty():
            raise ValueError(f"La cola {self.nombre} está vacía")
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return valor

    def peek(self):
        if self.is_empty():
            raise ValueError(f"La cola {self.nombre} está vacía")
        return self.frente.valor

    def __str__(self):
        elementos = []
        actual = self.frente
        while actual:
            elementos.append(str(actual.valor))
            actual = actual.siguiente
        return f"Cola {self.nombre}: {' -> '.join(elementos)}"

if __name__ == "__main__":
    cola1 = ColaEnlazada("A")
    cola2 = ColaEnlazada("B")
    
    cola1.enqueue(1)
    cola1.enqueue(2)
    cola1.enqueue(3)
    
    cola2.enqueue(4)
    cola2.enqueue(5)
    cola2.enqueue(6)
    
    print(cola1)
    print(cola2)
    
    print("Elemento al frente de la cola A:", cola1.peek())
    print("Elemento al frente de la cola B:", cola2.peek())
    
    print("Elemento eliminado de la cola A:", cola1.dequeue())
    print("Elemento eliminado de la cola B:", cola2.dequeue())
    
    print(cola1)
    print(cola2)
    
    print("¿Está vacía la cola A?", cola1.is_empty())
    print("¿Está vacía la cola B?", cola2.is_empty())
