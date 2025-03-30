class Nodo:
    """Nodo individual de la lista enlazada"""
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class MyLinkedList:
    """Lista enlazada con operaciones básicas"""
    
    def __init__(self):
        """Inicializa la lista vacía"""
        self.cabeza = None
        self.cola = None
        self.tamaño = 0

    def __len__(self):
        """Devuelve el número de elementos en la lista"""
        return self.tamaño

    def __str__(self):
        """Representación en cadena de la lista"""
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.valor))
            actual = actual.siguiente
        return ' → '.join(elementos)

    def insertar_al_inicio(self, valor):
        """Inserta un nuevo nodo al inicio de la lista"""
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self.tamaño += 1

    def insertar_al_final(self, valor):
        """Inserta un nuevo nodo al final de la lista"""
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamaño += 1

    def eliminar_al_inicio(self):
        """Elimina el primer nodo de la lista"""
        if not self.cabeza:
            raise ValueError("Lista vacía")
        valor = self.cabeza.valor
        self.cabeza = self.cabeza.siguiente
        if not self.cabeza:
            self.cola = None
        self.tamaño -= 1
        return valor

    def eliminar_al_final(self):
        """Elimina el último nodo de la lista"""
        if not self.cabeza:
            raise ValueError("Lista vacía")
        valor = self.cola.valor
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            actual = self.cabeza
            while actual.siguiente != self.cola:
                actual = actual.siguiente
            actual.siguiente = None
            self.cola = actual
        self.tamaño -= 1
        return valor

    def buscar(self, valor):
        """Busca un valor en la lista y devuelve su posición"""
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.valor == valor:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1

    def obtener(self, posicion):
        """Devuelve el valor en una posición específica"""
        if posicion < 0 or posicion >= self.tamaño:
            raise IndexError("Posición fuera de rango")
        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        return actual.valor

if __name__ == "__main__":
    mi_lista = MyLinkedList()
    
    mi_lista.insertar_al_final(10)
    mi_lista.insertar_al_final(20)
    mi_lista.insertar_al_inicio(5)
    
    print("Lista:", mi_lista)
    
    print("Tamaño:", len(mi_lista)) 
    print("Buscar 10:", mi_lista.buscar(10))
    print("Obtener posición 2:", mi_lista.obtener(2))
    
    print("Eliminar inicio:", mi_lista.eliminar_al_inicio())
    print("Lista después de eliminar:", mi_lista)
