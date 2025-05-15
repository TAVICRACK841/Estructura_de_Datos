# Crear un diccionario (tabla hash)
agenda = {
    "Ana": "555-1234",
    "Luis": "555-5678",
    "Carlos": "555-8765",
    "María": "555-4321"
}

# Buscar el teléfono de una persona
nombre = "Carlos"
if nombre in agenda:
    print(f"El teléfono de {nombre} es {agenda[nombre]}")
else:
    print(f"{nombre} no está en la agenda.")
