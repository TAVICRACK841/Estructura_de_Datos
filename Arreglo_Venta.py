def ingresar_datos():
    """Ingresa los datos de ventas mensuales."""
    meses = []
    ropa = []
    deportes = []
    jugueteria = []

    while True:
        mes = input("Ingrese el nombre del mes (o 'fin' para terminar): ").capitalize()
        if mes == 'Fin':
            break

        while True:
            try:
                venta_ropa = float(input(f"Venta de ropa en {mes}: "))
                venta_deportes = float(input(f"Venta de deportes en {mes}: "))
                venta_jugueteria = float(input(f"Venta de jugueteria en {mes}: "))
                break  # Sale del bucle si las entradas son válidas
            except ValueError:
                print("Error: Ingrese un número válido.")

        meses.append(mes)
        ropa.append(venta_ropa)
        deportes.append(venta_deportes)
        jugueteria.append(venta_jugueteria)

    return meses, ropa, deportes, jugueteria


def buscar_elemento(meses, ropa, deportes, jugueteria):
    """Busca y muestra las ventas de un mes específico."""
    mes_buscar = input("Ingrese el mes a buscar: ").capitalize()
    if mes_buscar in meses:
        indice = meses.index(mes_buscar)
        print(f"Ventas en {mes_buscar}:")
        print(f"  Ropa: ${ropa[indice]:.2f}")
        print(f"  Deportes: ${deportes[indice]:.2f}")
        print(f"  Juguetería: ${jugueteria[indice]:.2f}")
    else:
        print("Mes no encontrado.")


def eliminar_venta(meses, ropa, deportes, jugueteria):
    """Elimina las ventas de un mes específico."""
    mes_eliminar = input("Ingrese el mes a eliminar: ").capitalize()
    if mes_eliminar in meses:
        indice = meses.index(mes_eliminar)
        del meses[indice]
        del ropa[indice]
        del deportes[indice]
        del jugueteria[indice]
        print(f"Ventas de {mes_eliminar} eliminadas.")
    else:
        print("Mes no encontrado.")


def mostrar_menu(meses, ropa, deportes, jugueteria):
    """Muestra el menú de opciones y gestiona la interacción con el usuario."""
    while True:
        print("\n--- Menú ---")
        print("1. Ingresar datos de ventas")
        print("2. Buscar ventas por mes")
        print("3. Eliminar ventas de un mes")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            meses, ropa, deportes, jugueteria = ingresar_datos()
        elif opcion == '2':
            buscar_elemento(meses, ropa, deportes, jugueteria)
        elif opcion == '3':
            eliminar_venta(meses, ropa, deportes, jugueteria)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# Inicialización de los arreglos
meses = []
ropa = []
deportes = []
jugueteria = []

# Inicia el menú
mostrar_menu(meses, ropa, deportes, jugueteria)
