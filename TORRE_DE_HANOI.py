class Pila:
    def __init__(self, nombre):
        self.elementos = []
        self.nombre = nombre
    
    def apilar(self, elemento):
        self.elementos.append(elemento)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def ver_tope(self):
        return self.elementos[-1] if not self.esta_vacia() else None

def dibujar_torres(A, B, C):
    max_altura = max(len(A.elementos), len(B.elementos), len(C.elementos))
    
    for nivel in range(max_altura-1, -1, -1):
        fila = []
        for torre in [A, B, C]:
            if nivel < len(torre.elementos):
                fila.append(f'{"■" * torre.elementos[nivel]:^5}')
            else:
                fila.append(f'{"|":^5}')
        print(' '.join(fila))
    
    print(f'{"A":^5} {"B":^5} {"C":^5}\n{"═"*20}')

def mover_disco(origen, destino):
    disco = origen.desapilar()
    destino.apilar(disco)
    print(f"🔥 Moviendo disco {disco} de {origen.nombre} → {destino.nombre}")
    dibujar_torres(A, B, C)

def resolver_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        mover_disco(origen, destino)
    else:
        resolver_hanoi(n-1, origen, auxiliar, destino)
        mover_disco(origen, destino)
        resolver_hanoi(n-1, auxiliar, destino, origen)

A = Pila("A")
B = Pila("B")
C = Pila("C")

for disco in [3, 2, 1]:
    A.apilar(disco)

print("🏰 ESTADO INICIAL DE LAS TORRES 🏰")
dibujar_torres(A, B, C)

resolver_hanoi(3, A, C, B)

print("✨ ¡TORRES DE HANÓI RESUELTAS! ✨")
