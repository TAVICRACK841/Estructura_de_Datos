# **Memoria Estática (simulada):**
# En Python, las tuplas son inmutables (tamaño fijo después de la creación).
calificaciones_estaticas = (90, 85, 95)  # Tamaño fijo de 3 elementos

print("Memoria Estática (simulada) - Calificaciones:", calificaciones_estaticas)

# **Memoria Dinámica:**
# Las listas en Python permiten agregar y eliminar elementos dinámicamente.
calificaciones_dinamicas = [95, 88, 92]

print("\nMemoria Dinámica - Calificaciones:", calificaciones_dinamicas)

# Agregando un elemento
calificaciones_dinamicas.append(76)
print("\nMemoria Dinámica - Calificaciones (después de agregar un elemento):", calificaciones_dinamicas)

# Eliminando un elemento
calificaciones_dinamicas.remove(88)  # Elimina el valor 88
print("\nMemoria Dinámica - Calificaciones (después de eliminar un elemento):", calificaciones_dinamicas)