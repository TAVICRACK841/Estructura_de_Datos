class Pila:
    def __init__(self):
        self.elementos = []
    
    def apilar(self, elemento):
        self.elementos.append(elemento)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None
    
    def esta_vacia(self):
        return len(self.elementos) == 0

def evaluar_posfija(expresion):
    pila = Pila()
    operadores = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else float('inf')
    }
    
    tokens = expresion.split()
    
    for token in tokens:
        if token in operadores:
            if len(pila.elementos) < 2:
                return None, "Error: Faltan operandos"
            b = pila.desapilar()
            a = pila.desapilar()
            try:
                resultado = operadores[token](a, b)
            except ZeroDivisionError:
                return None, "Error: División por cero"
            pila.apilar(resultado)
        else:
            try:
                pila.apilar(float(token))
            except ValueError:
                return None, f"Error: Token inválido '{token}'"
    
    if len(pila.elementos) != 1:
        return None, "Error: Expresión incompleta"
    return pila.desapilar(), None

def evaluar_prefija(expresion):
    pila = Pila()
    operadores = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else float('inf')
    }
    
    tokens = reversed(expresion.split()) 
    
    for token in tokens:
        if token in operadores:
            if len(pila.elementos) < 2:
                return None, "Error: Faltan operandos"
            a = pila.desapilar()
            b = pila.desapilar()
            try:
                resultado = operadores[token](a, b)
            except ZeroDivisionError:
                return None, "Error: División por cero"
            pila.apilar(resultado)
        else:
            try:
                pila.apilar(float(token))
            except ValueError:
                return None, f"Error: Token inválido '{token}'"
    
    if len(pila.elementos) != 1:
        return None, "Error: Expresión incompleta"
    return pila.desapilar(), None

def main():
    print("""
    ░██████╗░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░
    ██╔════╝██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░
    ╚█████╗░██║░░██║██║░░░░░██║░░██║██║░░░██║██║░░░░░
    ░╚═══██╗██║░░██║██║░░░░░██║░░██║██║░░░██║██║░░░░░
    ██████╔╝╚█████╔╝███████╗╚█████╔╝╚██████╔╝███████╗
    ╚═════╝░░╚════╝░╚══════╝░╚════╝░░╚═════╝░╚══════╝
    """)
    
    while True:
        print("\n1. Evaluar notación posfija (Ej: 3 4 + 2 *)")
        print("2. Evaluar notación prefija (Ej: * + 3 4 2)")
        print("3. Salir")
        opcion = input("\nSeleccione una opción (1-3): ")
        
        if opcion == '3':
            print("\n¡Hasta luego! 👋")
            break
            
        if opcion not in ('1', '2'):
            print("\n⚠️ Opción inválida. Intente nuevamente.")
            continue
            
        expresion = input("\nIngrese la expresión (separada por espacios): ")
        
        if opcion == '1':
            resultado, error = evaluar_posfija(expresion)
        else:
            resultado, error = evaluar_prefija(expresion)
        
        if error:
            print(f"\n🔴 {error}")
        else:
            print(f"\n🟢 Resultado: {resultado}")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
