def merge(lista, inicio, medio, fin):
    izquierda = lista[inicio:medio+1]
    derecha = lista[medio+1:fin+1]

    i = 0
    j = 0
    k = inicio

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i]["nombre"].lower() <= derecha[j]["nombre"].lower():
            lista[k] = izquierda[i]
            i += 1
        else:
            lista[k] = derecha[j]
            j += 1
        k += 1

    while i < len(izquierda):
        lista[k] = izquierda[i]
        i += 1
        k += 1

    while j < len(derecha):
        lista[k] = derecha[j]
        j += 1
        k += 1

def mezcla_directa(lista):
    n = len(lista)
    tamaño = 1
    while tamaño < n:
        inicio = 0
        while inicio < n - tamaño:
            medio = inicio + tamaño - 1
            fin = min(inicio + 2*tamaño - 1, n - 1)
            merge(lista, inicio, medio, fin)
            inicio += 2*tamaño
        tamaño *= 2

def mezcla_equilibrada(lista, inicio, fin):
    if inicio < fin:
        medio = (inicio + fin) // 2
        mezcla_equilibrada(lista, inicio, medio)
        mezcla_equilibrada(lista, medio + 1, fin)
        merge(lista, inicio, medio, fin)

def mostrar_empleados(empleados):
    print(f"\n{'Nombre':<15} {'Estado Civil':<15} {'Antigüedad':<12} {'Categoría':<10} {'Sueldo':<10}")
    print("-" * 65)
    for e in empleados:
        print(f"{e['nombre']:<15} {e['estado_civil']:<15} {e['antiguedad']:<12} {e['categoria']:<10} {e['sueldo']:<10.2f}")

def cargar_empleados():
    # Simulación de datos leídos desde archivo EMPLEADOS
    return [
        {"nombre": "Ana", "estado_civil": "Soltera", "antiguedad": 5, "categoria": "A", "sueldo": 2500.0},
        {"nombre": "Carlos", "estado_civil": "Casado", "antiguedad": 10, "categoria": "B", "sueldo": 3200.0},
        {"nombre": "Luis", "estado_civil": "Soltero", "antiguedad": 3, "categoria": "C", "sueldo": 2100.0},
        {"nombre": "Beatriz", "estado_civil": "Casada", "antiguedad": 7, "categoria": "A", "sueldo": 2800.0},
        {"nombre": "Daniel", "estado_civil": "Soltero", "antiguedad": 2, "categoria": "B", "sueldo": 2300.0}
    ]

def menu():
    empleados = cargar_empleados()
    while True:
        print("\n--- Menú de ordenamiento de empleados ---")
        print("1. Mostrar empleados sin ordenar")
        print("2. Ordenar empleados por nombre con mezcla directa")
        print("3. Ordenar empleados por nombre con mezcla equilibrada")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_empleados(empleados)
        elif opcion == "2":
            empleados_md = empleados.copy()
            mezcla_directa(empleados_md)
            print("\nEmpleados ordenados con mezcla directa:")
            mostrar_empleados(empleados_md)
        elif opcion == "3":
            empleados_me = empleados.copy()
            mezcla_equilibrada(empleados_me, 0, len(empleados_me) - 1)
            print("\nEmpleados ordenados con mezcla equilibrada:")
            mostrar_empleados(empleados_me)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
