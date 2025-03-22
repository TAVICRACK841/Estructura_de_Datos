class NodoPostre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = None
        self.siguiente = None

class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

class GestorPostres:
    def __init__(self):
        self.cabecera = None
    
    def _insertar_ordenado(self, nombre):
        nuevo = NodoPostre(nombre)
        if not self.cabecera or self.cabecera.nombre > nombre:
            nuevo.siguiente = self.cabecera
            self.cabecera = nuevo
        else:
            actual = self.cabecera
            while actual.siguiente and actual.siguiente.nombre < nombre:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        return nuevo
    
    def _buscar_postre(self, nombre):
        actual = self.cabecera
        while actual:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
        return None
    
    def _agregar_ingrediente(self, postre, ingrediente):
        nuevo = NodoIngrediente(ingrediente)
        if not postre.ingredientes:
            postre.ingredientes = nuevo
        else:
            actual = postre.ingredientes
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
    
    def _eliminar_ingrediente(self, postre, ingrediente):
        actual = postre.ingredientes
        previo = None
        while actual:
            if actual.nombre == ingrediente:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    postre.ingredientes = actual.siguiente
                return True
            previo = actual
            actual = actual.siguiente
        return False
    
    def mostrar_ingredientes(self, nombre):
        postre = self._buscar_postre(nombre)
        if not postre:
            print("Postre no encontrado!")
            return
        
        print(f"\nIngredientes de {nombre}:")
        ingrediente = postre.ingredientes
        if not ingrediente:
            print("No hay ingredientes registrados")
        while ingrediente:
            print(f"- {ingrediente.nombre}")
            ingrediente = ingrediente.siguiente
    
    def agregar_ingredientes(self, nombre):
        postre = self._buscar_postre(nombre)
        if not postre:
            print("Postre no encontrado!")
            return
        
        nuevos = input("Ingrese nuevos ingredientes (separados por coma): ").split(',')
        for ing in nuevos:
            ing = ing.strip()
            if not self._ingrediente_existe(postre, ing):
                self._agregar_ingrediente(postre, ing)
                print(f"'{ing}' agregado")
            else:
                print(f"'{ing}' ya existe")
    
    def _ingrediente_existe(self, postre, ingrediente):
        actual = postre.ingredientes
        while actual:
            if actual.nombre == ingrediente:
                return True
            actual = actual.siguiente
        return False
    
    def eliminar_ingrediente(self, nombre):
        postre = self._buscar_postre(nombre)
        if not postre:
            print("Postre no encontrado!")
            return
        
        ingrediente = input("Ingrediente a eliminar: ").strip()
        if self._eliminar_ingrediente(postre, ingrediente):
            print(f"'{ingrediente}' eliminado")
        else:
            print("Ingrediente no encontrado")
    
    def alta_postre(self):
        nombre = input("Nombre del nuevo postre: ").strip()
        if self._buscar_postre(nombre):
            print("¡Este postre ya existe!")
            return
        
        nuevos = input("Ingredientes iniciales (separados por coma): ").split(',')
        nuevo_postre = self._insertar_ordenado(nombre)
        for ing in nuevos:
            self._agregar_ingrediente(nuevo_postre, ing.strip())
        print("Postre creado exitosamente!")
    
    def baja_postre(self):
        nombre = input("Nombre del postre a eliminar: ").strip()
        actual = self.cabecera
        previo = None
        
        while actual:
            if actual.nombre == nombre:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.cabecera = actual.siguiente
                print("Postre eliminado!")
                return
            previo = actual
            actual = actual.siguiente
        print("Postre no encontrado!")
    
    def eliminar_repetidos(self):
        actual = self.cabecera
        while actual:
            vistos = set()
            current = actual.ingredientes
            prev = None
            
            while current:
                if current.nombre in vistos:
                    prev.siguiente = current.siguiente
                else:
                    vistos.add(current.nombre)
                    prev = current
                current = current.siguiente
            actual = actual.siguiente
        print("Duplicados eliminados en todos los postres!")

def main():
    gestor = GestorPostres()
    while True:
        print("\n--- MENÚ POSTRES ---")
        print("Postres disponibles:")
        postres = []
        actual = gestor.cabecera
        while actual:
            postres.append(actual.nombre)
            actual = actual.siguiente
        print(f"\n{' | '.join(postres)}")
        
        print("\nOpciones:")
        print("1. Mostrar ingredientes (A)")
        print("2. Agregar ingredientes (B)")
        print("3. Eliminar ingrediente (C)")
        print("4. Alta postre (D)")
        print("5. Baja postre (E)")
        print("6. Eliminar repetidos (Subprograma)")
        print("7. Salir")
        
        opcion = input("\nSeleccione opción: ")
        
        if opcion == "1":
            gestor.mostrar_ingredientes(input("Nombre del postre: ").strip())
        elif opcion == "2":
            gestor.agregar_ingredientes(input("Nombre del postre: ").strip())
        elif opcion == "3":
            gestor.eliminar_ingrediente(input("Nombre del postre: ").strip())
        elif opcion == "4":
            gestor.alta_postre()
        elif opcion == "5":
            gestor.baja_postre()
        elif opcion == "6":
            gestor.eliminar_repetidos()
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida!")

if __name__ == "__main__":
    main()