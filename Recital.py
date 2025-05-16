def merge_three_lists(lista1, lista2, lista3):
    i = j = k = 0
    resultado = []

    while i < len(lista1) or j < len(lista2) or k < len(lista3):
        candidatos = []

        if i < len(lista1):
            candidatos.append((lista1[i]["nombre"].lower(), 'lista1'))
        if j < len(lista2):
            candidatos.append((lista2[j]["nombre"].lower(), 'lista2'))
        if k < len(lista3):
            candidatos.append((lista3[k]["nombre"].lower(), 'lista3'))

        if not candidatos:
            break

        menor = min(candidatos, key=lambda x: x[0])[1]

        if menor == 'lista1':
            resultado.append(lista1[i])
            i += 1
        elif menor == 'lista2':
            resultado.append(lista2[j])
            j += 1
        else:
            resultado.append(lista3[k])
            k += 1

    return resultado

def mostrar_recitales(recitales):
    if not recitales:
        print("\nEl archivo RECITALES está vacío.")
        return
    print(f"\n{'Nombre':<25} {'Nº Presentaciones':<20} {'Fechas':<30}")
    print("-" * 75)
    for r in recitales:
        fechas_str = ", ".join(r["fechas"])
        print(f"{r['nombre']:<25} {r['presentaciones']:<20} {fechas_str:<30}")

def ingresar_recitales(nombre_lista):
    recitales = []
    n = int(input(f"\n¿Cuántos registros desea ingresar para {nombre_lista}? "))
    for i in range(n):
        print(f"\nRegistro #{i+1} de {nombre_lista}:")
        nombre = input("Nombre del cantante u orquesta: ").strip()
        presentaciones = int(input("Número de presentaciones: "))
        fechas = []
        for f in range(presentaciones):
            fecha = input(f"Fecha de presentación #{f+1} (formato YYYY-MM-DD): ").strip()
            fechas.append(fecha)
        recitales.append({
            "nombre": nombre,
            "presentaciones": presentaciones,
            "fechas": fechas
        })
    # Ordenar la lista por nombre para mantener el requisito
    recitales.sort(key=lambda x: x["nombre"].lower())
    return recitales

def menu():
    A1 = []
    A2 = []
    A3 = []
    recitales = []

    while True:
        print("\n--- Menú de gestión de archivos RECITALES ---")
        print("1. Ingresar datos para archivo A1")
        print("2. Ingresar datos para archivo A2")
        print("3. Ingresar datos para archivo A3")
        print("4. Intercalar los tres archivos y formar RECITALES")
        print("5. Mostrar archivo RECITALES")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            A1 = ingresar_recitales("archivo A1")
            print(f"\nDatos ingresados para A1 (ordenados por nombre).")
        elif opcion == "2":
            A2 = ingresar_recitales("archivo A2")
            print(f"\nDatos ingresados para A2 (ordenados por nombre).")
        elif opcion == "3":
            A3 = ingresar_recitales("archivo A3")
            print(f"\nDatos ingresados para A3 (ordenados por nombre).")
        elif opcion == "4":
            if not A1 or not A2 or not A3:
                print("\nDebe ingresar datos en los tres archivos antes de intercalar.")
            else:
                recitales = merge_three_lists(A1, A2, A3)
                print("\nArchivos intercalados correctamente en RECITALES.")
        elif opcion == "5":
            mostrar_recitales(recitales)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
