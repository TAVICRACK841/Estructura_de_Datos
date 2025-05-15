# Crear una tabla hash de tamaño 10
hash_table = [None] * 10

# Lista de números a insertar
numeros = [34, 16, 2, 93, 80, 77, 51]

# Insertar los números en la tabla hash usando la función hash simple: valor % 10
for numero in numeros:
    hash_table[numero % 10] = numero

# Función para buscar un número en la tabla hash
def buscar_numero_hash(key, hash_table):
    if hash_table[key % 10] == key:
        return key % 10
    else:
        return None

# Ejemplo de búsqueda
numero_a_buscar = 93
posicion = buscar_numero_hash(numero_a_buscar, hash_table)
if posicion is not None:
    print(f"El número {numero_a_buscar} está en la posición {posicion} de la tabla hash.")
else:
    print(f"El número {numero_a_buscar} no está en la tabla hash.")
