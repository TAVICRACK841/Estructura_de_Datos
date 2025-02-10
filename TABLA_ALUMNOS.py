import numpy as np
import random

def generar_nombre(tipo, numero):
    """Genera nombres automáticos para alumnos o materias."""
    if tipo == "alumno":
        return f"Alumno {numero}"
    elif tipo == "materia":
        return f"Materia {numero}"
    else:
        return "Desconocido"

def crear_arreglo(num_alumnos, num_materias):
    arreglo = np.zeros((num_materias, num_alumnos), dtype=object)
    nombres_alumnos = [generar_nombre("alumno", i+1) for i in range(num_alumnos)]
    nombres_materias = [generar_nombre("materia", i+1) for i in range(num_materias)]

    return arreglo, nombres_alumnos, nombres_materias

def asignar_calificaciones_automaticas(arreglo):
    for i in range(arreglo.shape[0]):
        for j in range(arreglo.shape[1]):
            arreglo[i, j] = random.randint(0, 100)

def buscar_alumno_materia(arreglo, nombres_alumnos, nombres_materias, alumno_id, materia_id):
    try:
        alumno_index = alumno_id - 1
        materia_index = materia_id - 1
        
        alumno_nombre = nombres_alumnos[alumno_index]
        materia_nombre = nombres_materias[materia_index]
        
        valor = arreglo[materia_index, alumno_index]
        print(f"Calificación de {alumno_nombre} en {materia_nombre}: {valor}")
    except IndexError:
        print("Alumno o materia no encontrados.")

def mostrar_tabla(arreglo, nombres_alumnos, nombres_materias):
    print(" " * 12, end="")
    for alumno in nombres_alumnos:
        print(f"{alumno:12}", end="")
    print()

    for i, materia in enumerate(nombres_materias):
        print(f"{materia:12}", end="") 
        for j in range(arreglo.shape[1]):
            print(f"{arreglo[i, j]:12}", end="")
        print()

def cambiar_forma_tabla(arreglo, nombres_alumnos, nombres_materias):
    arreglo_transpuesto = arreglo.T
    return arreglo_transpuesto, nombres_materias, nombres_alumnos

def menu():
    num_alumnos = int(input("Ingrese la cantidad de alumnos: "))
    num_materias = int(input("Ingrese la cantidad de materias: "))

    arreglo, nombres_alumnos, nombres_materias = crear_arreglo(num_alumnos, num_materias)

    while True:
        print("\n--- Menú ---")
        print("1. Asignar calificaciones automáticas")
        print("2. Mostrar tabla")
        print("3. Buscar alumno y materia")
        print("4. Cambiar la forma de la tabla")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            asignar_calificaciones_automaticas(arreglo)
            print("Calificaciones asignadas automáticamente.")
        elif opcion == "2":
            mostrar_tabla(arreglo, nombres_alumnos, nombres_materias)
        elif opcion == "3":
            alumno_id = int(input("Ingrese el número de alumno a buscar: "))
            materia_id = int(input("Ingrese el número de materia a buscar: "))
            buscar_alumno_materia(arreglo, nombres_alumnos, nombres_materias, alumno_id, materia_id)
        elif opcion == "4":
            arreglo, nombres_alumnos, nombres_materias = cambiar_forma_tabla(arreglo, nombres_alumnos, nombres_materias)
            print("Forma de la tabla cambiada.")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()