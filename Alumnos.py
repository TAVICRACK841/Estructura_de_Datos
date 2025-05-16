def seleccion_directa(alumnos):
    n = len(alumnos)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if alumnos[j]["nombre"].lower() < alumnos[min_idx]["nombre"].lower():
                min_idx = j
        if min_idx != i:
            alumnos[i], alumnos[min_idx] = alumnos[min_idx], alumnos[i]

def particion(alumnos, low, high):
    pivot = alumnos[high]["materias"]
    i = low - 1
    for j in range(low, high):
        if alumnos[j]["materias"] < pivot:
            i += 1
            alumnos[i], alumnos[j] = alumnos[j], alumnos[i]
    alumnos[i + 1], alumnos[high] = alumnos[high], alumnos[i + 1]
    return i + 1

def quicksort(alumnos, low, high):
    if low < high:
        pi = particion(alumnos, low, high)
        quicksort(alumnos, low, pi - 1)
        quicksort(alumnos, pi + 1, high)

def mostrar_alumnos(alumnos):
    print("\nLista de alumnos:")
    print(f"{'Nombre':<15} {'Matrícula':<10} {'Materias':<10} {'Promedio':<8}")
    print("-" * 45)
    for a in alumnos:
        print(f"{a['nombre']:<15} {a['matricula']:<10} {a['materias']:<10} {a['promedio']:<8.2f}")

def ingresar_alumnos():
    alumnos = []
    n = int(input("¿Cuántos alumnos desea ingresar? "))
    for i in range(n):
        print(f"\nIngrese datos del alumno #{i+1}:")
        nombre = input("Nombre: ")
        matricula = input("Matrícula: ")
        materias = int(input("Número de materias aprobadas: "))
        promedio = float(input("Promedio: "))
        alumnos.append({
            "nombre": nombre,
            "matricula": matricula,
            "materias": materias,
            "promedio": promedio
        })
    return alumnos

def menu():
    alumnos = ingresar_alumnos()
    while True:
        print("\nMenú de opciones:")
        print("1. Ordenar por nombre (Selección directa)")
        print("2. Ordenar por número de materias aprobadas (Quicksort)")
        print("3. Mostrar lista actual")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            seleccion_directa(alumnos)
            print("\nAlumnos ordenados por nombre (ascendente).")
            mostrar_alumnos(alumnos)
        elif opcion == "2":
            quicksort(alumnos, 0, len(alumnos) - 1)
            print("\nAlumnos ordenados por número de materias aprobadas (ascendente).")
            mostrar_alumnos(alumnos)
        elif opcion == "3":
            mostrar_alumnos(alumnos)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
