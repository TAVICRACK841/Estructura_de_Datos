hoteles = []

n = int(input("¿Cuántos hoteles desea ingresar? "))

for i in range(n):
    print(f"\nIngrese los datos del hotel #{i+1}:")
    nombre = input("Nombre del hotel: ")
    ciudad = input("Ciudad: ")
    estrellas = int(input("Número de estrellas: "))
    cuartos = int(input("Número de cuartos: "))
    hotel = {
        "nombre": nombre,
        "ciudad": ciudad,
        "estrellas": estrellas,
        "cuartos": cuartos
    }
    hoteles.append(hotel)

hoteles_ordenados = sorted(hoteles, key=lambda x: (x["ciudad"], x["nombre"]))

print("\nHoteles ordenados por ciudad y nombre:")
for hotel in hoteles_ordenados:
    print(f"{hotel['nombre']} - {hotel['ciudad']} - {hotel['estrellas']} estrellas - {hotel['cuartos']} cuartos")
