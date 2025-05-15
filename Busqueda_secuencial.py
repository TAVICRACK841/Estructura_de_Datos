def busqueda_secuencial(lista, valor):
    for i, elemento in enumerate(lista):
        if elemento == valor:
            return i
    return None

nombres = ["Ana", "Luis", "Carlos", "María", "Sofía"]
buscado = "Carlos"
resultado = busqueda_secuencial(nombres, buscado)

if resultado is not None:
    print(f'El nombre {buscado} se encuentra en la posición {resultado}')
else:
    print(f'El nombre {buscado} no se encuentra en la lista')
