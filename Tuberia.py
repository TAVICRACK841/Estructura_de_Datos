import time

class Tuberia:
    def __init__(self, capacidad):
        self.datos = []
        self.capacidad = capacidad

    def agregar_dato(self, dato):
        if len(self.datos) < self.capacidad:
            self.datos.append(dato)
            print(f"Se ha agregado {dato} a la tubería.")
            if len(self.datos) == self.capacidad:
                print("La tubería está llena.")
        else:
            print("La tubería está llena. No se puede agregar más datos.")

    def extraer_dato(self):
        if self.datos:
            dato = self.datos.pop(0)
            print(f"Se ha extraído {dato} de la tubería.")
            if not self.datos:
                print("La tubería está vacía.")
        else:
            print("La tubería está vacía.")

    def pasar_datos(self, destino):
        while self.datos:
            dato = self.datos.pop(0)
            destino.agregar_dato(dato)
            print(f"Se ha pasado {dato} a la tubería de destino.")

    def imprimir_datos(self):
        print("Datos en la tubería:", self.datos)


# Ejemplo de uso
if __name__ == "__main__":
    # Inicializar tuberías
    tuberia1 = Tuberia(5)
    tuberia2 = Tuberia(5)

    # Mostrar estado inicial
    print("\nEstado inicial:")
    print("Tubería 1 (vacía):", tuberia1.datos)
    print("Tubería 2 (vacía):", tuberia2.datos)
    time.sleep(2)  # Esperar 2 segundos

    # Agregar datos a la tubería 1
    print("\nAgregando datos a la tubería 1:")
    for dato in ["Dato1", "Dato2", "Dato3", "Dato4", "Dato5"]:
        tuberia1.agregar_dato(dato)
        time.sleep(1)  # Esperar 1 segundo entre cada dato

    # Mostrar tubería llena
    print("\nEstado después de agregar datos:")
    print("Tubería 1 (llena):", tuberia1.datos)
    print("Tubería 2 (vacía):", tuberia2.datos)
    time.sleep(2)

    # Pasar datos a la tubería 2
    print("\nPasando datos a la tubería 2:")
    tuberia1.pasar_datos(tuberia2)
    time.sleep(2)

    # Mostrar estado final
    print("\nEstado final:")
    print("Tubería 1 (vacía):", tuberia1.datos)
    print("Tubería 2 (llena):", tuberia2.datos)
    time.sleep(2)