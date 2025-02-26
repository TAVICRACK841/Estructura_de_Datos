import random

def llenar_vector(tamaño):
    return [random.randint(-100, 100) for _ in range(tamaño)]

def mostrar_vector(vector, nombre):
    print(f"Vector {nombre}: {vector}")

def main():
    tamaño = int(input("Ingrese el tamaño de los vectores: "))
    A, B, C = [], [], []

    while True:
        print("\nMenú:")
        print("1. Llenar Vector A de manera aleatoria.")
        print("2. Llenar Vector B de manera aleatoria.")
        print("3. Realizar C=A+B")
        print("4. Realizar C=B-A")
        print("5. Mostrar")
        print("6. Salir")

        opción = input("Ingrese su opción: ")

        if opción == "1":
            A = llenar_vector(tamaño)
        elif opción == "2":
            B = llenar_vector(tamaño)
        elif opción == "3":
            if A and B:
                C = [a + b for a, b in zip(A, B)]
            else:
                print("Vectores A y B deben estar llenos.")
        elif opción == "4":
            if A and B:
                C = [b - a for a, b in zip(A, B)]
            else:
                print("Vectores A y B deben estar llenos.")
        elif opción == "5":
            if A or B or C:
                print("¿Qué vector desea mostrar?")
                print("1. Vector A")
                print("2. Vector B")
                print("3. Vector C")
                elección = input("Ingrese su elección: ")
                if elección == "1" and A:
                    mostrar_vector(A, 'A')
                elif elección == "2" and B:
                    mostrar_vector(B, 'B')
                elif elección == "3" and C:
                    mostrar_vector(C, 'C')
                else:
                    print("Vector no disponible.")
            else:
                print("No hay vectores llenos para mostrar.")
        elif opción == "6":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
