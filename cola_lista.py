class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ColaEnlazada:
    def __init__(self):
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
            raise ValueError("La cola está vacía")
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return valor

    def insertar_en_posicion(self, valor, posicion):
        if posicion == 1:
            nuevo_nodo = Nodo(valor)
            nuevo_nodo.siguiente = self.frente
            self.frente = nuevo_nodo
            if self.final is None:
                self.final = nuevo_nodo
        else:
            actual = self.frente
            for _ in range(posicion - 2):
                if actual.siguiente is None:
                    break
                actual = actual.siguiente
            if actual.siguiente is None:
                self.enqueue(valor)
            else:
                nuevo_nodo = Nodo(valor)
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                if nuevo_nodo.siguiente is None:
                    self.final = nuevo_nodo

    def eliminar_en_posicion(self, posicion):
        if self.is_empty():
            raise ValueError("La cola está vacía")
        if posicion == 1:
            valor = self.frente.valor
            self.frente = self.frente.siguiente
            if self.frente is None:
                self.final = None
            return valor
        else:
            actual = self.frente
            for _ in range(posicion - 2):
                if actual.siguiente is None:
                    raise ValueError("Posición inválida")
                actual = actual.siguiente
            if actual.siguiente is None:
                raise ValueError("Posición inválida")
            valor = actual.siguiente.valor
            actual.siguiente = actual.siguiente.siguiente
            if actual.siguiente is None:
                self.final = actual
            return valor

    def mostrar_con_posicion(self):
        if self.is_empty():
            print("La cola está vacía")
        else:
            actual = self.frente
            posicion = 1
            while actual:
                print(f"Posición {posicion}: {actual.valor}")
                actual = actual.siguiente
                posicion += 1

    def __str__(self):
        elementos = []
        actual = self.frente
        while actual:
            elementos.append(str(actual.valor))
            actual = actual.siguiente
        return ' -> '.join(elementos)

def main():
    cola = ColaEnlazada()

    while True:
        print("\nOpciones:")
        print("1. Agregar nodo al final")
        print("2. Agregar nodo en posición específica")
        print("3. Eliminar nodo del frente")
        print("4. Eliminar nodo en posición específica")
        print("5. Mostrar cola con posiciones")
        print("6. Mostrar cola")
        print("7. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            valor = input("Ingrese el valor del nodo: ")
            cola.enqueue(valor)
            print(f"Nodo agregado: {valor}")
        elif opcion == "2":
            valor = input("Ingrese el valor del nodo: ")
            posicion = int(input("Ingrese la posición para agregar el nodo: "))
            cola.insertar_en_posicion(valor, posicion)
            print(f"Nodo agregado en posición {posicion}")
        elif opcion == "3":
            try:
                valor = cola.dequeue()
                print(f"Nodo eliminado: {valor}")
            except ValueError as e:
                print(e)
        elif opcion == "4":
            try:
                posicion = int(input("Ingrese la posición del nodo a eliminar: "))
                valor = cola.eliminar_en_posicion(posicion)
                print(f"Nodo eliminado en posición {posicion}: {valor}")
            except ValueError as e:
                print(e)
        elif opcion == "5":
            cola.mostrar_con_posicion()
        elif opcion == "6":
            if cola.is_empty():
                print("La cola está vacía")
            else:
                print("Cola:", cola)
        elif opcion == "7":
            print("Saliendo del programa")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
