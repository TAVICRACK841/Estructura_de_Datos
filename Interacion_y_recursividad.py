def factorial_iterativo(n):
    """
    Calcula el factorial de un número de forma iterativa.
    """
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def factorial_recursivo(n):
    """
    Calcula el factorial de un número de forma recursiva.
    """
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    """
    print("\n--- Menú ---")
    print("1. Calcular factorial (iterativo)")
    print("2. Calcular factorial (recursivo)")
    print("3. Salir")

def main():
    """
    Función principal que controla el flujo del programa.
    """
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                n = int(input("Ingrese un número entero no negativo: "))
                if n < 0:
                    print("Por favor, ingrese un número no negativo.")
                else:
                    resultado = factorial_iterativo(n)
                    print(f"El factorial de {n} (iterativo) es: {resultado}")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")

        elif opcion == '2':
            try:
                n = int(input("Ingrese un número entero no negativo: "))
                if n < 0:
                    print("Por favor, ingrese un número no negativo.")
                else:
                    resultado = factorial_recursivo(n)
                    print(f"El factorial de {n} (recursivo) es: {resultado}")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")

        elif opcion == '3':
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()
