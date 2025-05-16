def busqueda_secuencial(alumnos, nombre_buscar):
    for alumno in alumnos:
        if alumno["nombre"].lower() == nombre_buscar.lower():
            return alumno
    return None

def busqueda_binaria(alumnos, nombre_buscar):
    bajo = 0
    alto = len(alumnos) - 1
    nombre_buscar = nombre_buscar.lower()

    while bajo <= alto:
        medio = (bajo + alto) // 2
        nombre_medio = alumnos[medio]["nombre"].lower()

        if nombre_medio == nombre_buscar:
            return alumnos[medio]
        elif nombre_medio < nombre_buscar:
            bajo = medio + 1
        else:
            alto = medio - 1
    return None

def mostrar_alumnos(alumnos):
    if not alumnos:
        print("\nNo hay alumnos en el arreglo.")
        return
    print(f"\n{'Nombre':<15} {'Promedio':<10} {'Materias Aprobadas':<18}")
    print("-" * 45)
    for a in alumnos:
        print(f"{a['nombre']:<15} {a['promedio']:<10.2f} {a['materias']:<18}")

def mostrar_resultado(resultado):
    if resultado:
        print(f"\nAlumno: {resultado['nombre']}")
        print(f"Promedio: {resultado['promedio']}")
        print(f"Materias aprobadas: {resultado['materias']}")
    else:
        print("\nEl alumno no se encuentra en el arreglo.")

def agregar_alumno(alumnos_desordenados):
    print("\nIngrese los datos del nuevo alumno:")
    nombre = input("Nombre: ").strip()
    while True:
        try:
            promedio = float(input("Promedio: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para el promedio.")
    while True:
        try:
            materias = int(input("Número de materias aprobadas: "))
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido para materias aprobadas.")

    nuevo_alumno = {
        "nombre": nombre,
        "promedio": promedio,
        "materias": materias
    }
    alumnos_desordenados.append(nuevo_alumno)
    print(f"\nAlumno '{nombre}' agregado correctamente.")

def main():
    alumnos_desordenados = [
        {"nombre": "Ana", "promedio": 8.5, "materias": 5},
        {"nombre": "Carlos", "promedio": 7.2, "materias": 6},
        {"nombre": "Luis", "promedio": 9.1, "materias": 7},
        {"nombre": "Beatriz", "promedio": 8.0, "materias": 4},
    ]

    # Inicialmente ordenamos la copia para búsqueda binaria
    alumnos_ordenados = sorted(alumnos_desordenados, key=lambda x: x["nombre"].lower())

    while True:
        print("\n--- Menú de gestión de alumnos ---")
        print("1. Ver alumnos (arreglo desordenado)")
        print("2. Ver alumnos (arreglo ordenado)")
        print("3. Agregar nuevo alumno")
        print("4. Buscar alumno en arreglo desordenado (búsqueda secuencial)")
        print("5. Buscar alumno en arreglo ordenado (búsqueda binaria)")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_alumnos(alumnos_desordenados)
        elif opcion == "2":
            mostrar_alumnos(alumnos_ordenados)
        elif opcion == "3":
            agregar_alumno(alumnos_desordenados)
            # Actualizar arreglo ordenado
            alumnos_ordenados = sorted(alumnos_desordenados, key=lambda x: x["nombre"].lower())
        elif opcion == "4":
            nombre = input("Ingrese el nombre del alumno a buscar: ")
            resultado = busqueda_secuencial(alumnos_desordenados, nombre)
            mostrar_resultado(resultado)
        elif opcion == "5":
            nombre = input("Ingrese el nombre del alumno a buscar: ")
            resultado = busqueda_binaria(alumnos_ordenados, nombre)
            mostrar_resultado(resultado)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
