class Pila:
    def __init__(self):
        self.elementos = []
    def apilar(self, elemento):
        self.elementos.append(elemento)
    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            return None
    def esta_vacia(self):
        return len(self.elementos) == 0
    def ver_pila(self):
        return self.elementos
    
if __name__ == "__main__":
    mi_pila = Pila()
    print("Pila vacía:", mi_pila.esta_vacia())
    mi_pila.apilar("Elemento 1")
    mi_pila.apilar("Elemento 2")
    mi_pila.apilar("Elemento 3") 
    print("Pila depués de apilar:", mi_pila.ver_pila())
    print("Pila vacía:", mi_pila.esta_vacia()) 
    elemento_desapilado = mi_pila.desapilar()
    print("Elemento desapilado:", elemento_desapilado)
    print("Pila después de desapilar:", mi_pila.ver_pila())       